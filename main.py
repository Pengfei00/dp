# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/10 16:35
"""

from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
import struct
import base64
from pyDes import des
import gzip
from model import decode_model
import logging
import socket
import random
import json
from io import BytesIO


class DPRequest:
    """
    flag:   0x66    HTTP_REQUEST
    flag:   0x67    HTTP_RESPONSE
    flag:   0x50    DISTRIBUTION_REQUEST
    flag:   0x3c    CREATE_KEY_REQUEST
    flag:   0x3d    CREATE_KEY_RESPONSE
    flag:   0x3e    CREATE_KEY_SUCCESS

    noSecurePayload={"b":decode_key,"i":"t"}
    """
    payload = None
    securePayload = None
    source = None
    flag = None
    isSecure = None
    totalLength = None
    array = None
    noSecureLength = None
    zip = None
    id = 0

    def __init__(self, des_key_b=None, des_key_t=None, des_key_a=None, localPublickey=None, localPrivate=None):
        self._ip = []
        self.AES_key = bytes.fromhex("")
        self.AES_iv = bytes.fromhex("")

        self._connecon = None
        self.des_key_b = des_key_b
        self.des_key_t = des_key_t
        self.des_key_a = des_key_a
        self.localPublickey = localPublickey
        self.localPrivate = localPrivate
        self.index = random.randint(140000000, 159999999)

    @property
    def conncon(self):
        if self._connecon:
            return self._connecon
        self._connecon = socket.socket()
        ip = self._ip[random.randint(0, len(self._ip) - 1)]
        logging.info("使用ip:{} 链接".format(ip))
        self._connecon.connect((ip, 443))
        return self._connecon

    def get_key(self):
        """
        self.local_publickey = keyPair.publickey().exportKey()[27:-24]
        self.local_private = keyPair.exportKey()[32:-29]
        :return:
        """
        logging.debug("生成rsakey")
        # 生成rsakey
        self._genRSAKeys()
        # 生成发送的公钥和设备信息
        # ff01003c00000001370000
        data = {'s': 0,
                'p': self.local_publickey[27:-24].decode(),
                'd': {'s': '19', 'p': '1440*900', 'b': '9cb6d01600139521', 'd': 'SM-G9350'}}
        data = self.make_data(securePayload=data, flag=0x3c, payload=False, isSecure=False)
        connecon = self.conncon
        logging.info("发送公钥")
        connecon.sendall(data)
        response = self.decode_data(connecon)

        # 0x3e CREATE_KEY_SUCCESS
        # ff01003e000000003a0038
        data = self.make_data(securePayload=None, flag=0x3e, post_data=None, payload=response, isSecure=False)
        logging.info("发送解码钥匙成功")
        connecon.sendall(data)
        logging.info("初始化成功 已获取所有参数")
        return True

    def unpack(self, fmt, stream):
        size = struct.calcsize(fmt)
        if isinstance(stream, BytesIO):
            buf = stream.read(size)
        elif isinstance(stream, str):
            buf = bytes.fromhex(stream)[:size]
        elif isinstance(stream, socket.socket):
            buf = stream.recv(size)
        else:
            return "类型错误"
        try:
            return struct.unpack(fmt, buf)
        except struct.error as e:
            logging.error("数据不全:{}".format(buf))

    """
    encrypt decrypt 模块
    
    """

    def make_data(self, securePayload, flag, post_data=None, payload=True, isSecure=True):
        if isinstance(securePayload, str):
            securePayload = securePayload.encode()
        elif isinstance(securePayload, dict):
            securePayload = json.dumps(securePayload).encode()
        elif securePayload is None:
            securePayload = b""
        if flag == 0x66:
            securePayload += b'\x00'

        if isinstance(payload, bool):
            payload = json.dumps(self.__payload).encode() if payload else b""
        elif isinstance(payload, dict):
            payload = json.dumps(payload).encode()
        elif isinstance(payload, str):
            payload = payload.encode()

        if securePayload and isSecure:
            encryptData = self.encrypt_by_des_cbc(securePayload + self.ne(post_data))
        else:
            encryptData = securePayload + self.ne(post_data)
        head = self.__get_head(payload, encryptData, flag, isSecure)

        return head + payload + encryptData

    @property
    def __payload(self):
        payload = {"b": self.des_key_b, "i": self.id, "t": self.des_key_t}
        logging.debug("生成payload:{}".format(payload))
        self.index += 1
        return payload

    def __get_head(self, payload, encryptData, flag, isSecure):
        noSecureLength = len(payload or "")
        totalLength = len(encryptData) + noSecureLength + 2
        data = struct.pack(">bbbbbih", -1, 0x1, 0x0, flag, isSecure, totalLength, noSecureLength)
        logging.debug("生成头部:{}".format(data.hex()))
        return data

    def _genRSAKeys(self):
        """
        生成本地的公钥密钥
        :return:
        """
        keyPair = RSA.generate(bits=1024)
        self.local_publickey = keyPair.publickey().exportKey()
        self.local_private = keyPair.exportKey()
        logging.debug("公钥:{}".format(self.local_publickey.decode()))
        logging.debug("私钥:{}".format(self.local_private.decode()))

    def encrypt_by_des_cbc(self, securePayload):
        """
        DES CBC 最后加密
        :param securePayload:
        :param post_data:
        :param key:
        :return:
        """
        logging.debug("开始DES_CBC加密:{}".format(securePayload))
        cipher = des(self.des_key_a[:8], padmode=2)
        result = cipher.encrypt(securePayload)
        logging.debug("DES_CBC加密结果:{}".format(result.hex()))
        return result

    def ne(self, data):
        """
        加密post_data
        :param data:
        :return:
        """
        if not data:
            return b""
        if isinstance(data, str):
            data = data.encode()
        elif isinstance(data, dict):
            data = json.dumps(data).encode()
        cipher = AES.new(self.AES_key, AES.MODE_CBC, self.AES_iv)
        result = cipher.decrypt(data)
        return result

    """
    decrypt 模块
    
    """

    def ndug(self, data, unzip=True):
        """
        解密response body
        :return:
        """
        if not data:
            return b""
        if isinstance(data, str):
            data = data.encode()
        cipher = AES.new(self.AES_key, AES.MODE_CBC, self.AES_iv)
        result = cipher.decrypt(data)
        if unzip:
            result = gzip.decompress(result)
        return result

    def decode_data(self, data):
        """
        解码消息并根据 flag进行处理
        :param data:
        :return:
        """
        _, _, _, flag, isSecure, totalLength, noSecureLength = self.unpack(">bbbbbih", data)

        func = hasattr(self, "decode_flag_{flag}".format(flag=flag))
        if func:
            func = getattr(self, "decode_flag_{flag}".format(flag=flag))
        else:
            print("错误flag:{flag}".format(flag=flag))

        func_data = func(data=data,
                         flag=flag,
                         isSecure=isSecure,
                         totalLength=totalLength,
                         noSecureLength=noSecureLength)
        return func_data

    def decrypt_by_des_cbc(self, data):
        if not isinstance(data, bytes):
            data = bytes.fromhex(data)
        cipher = des(key=self.des_key_a[:8], padmode=2)
        return cipher.decrypt(data)

    def decode_flag_70(self, data, totalLength, **kwargs):
        """
        0x46 好像每个response会先返回这个
        :param data:
        :param kwargs:
        :return:
        """
        response, = self.unpack(">{}s".format(totalLength - 2), data)
        logging.debug("response前置返回:{}".format(response.decode()))
        return self.decode_data(self.conncon)

    def decode_flag_61(self, data, totalLength, **kwargs):
        """
        获得创建密钥 之后还要发送获得成功回执
        0x3d CREATE_KEY_RESPONSE
        :param data:
        :param totalLength:
        :param kwargs:
        :return:
        """
        response, = self.unpack(">{}s".format(totalLength - 2), data)
        response = json.loads(response.decode())
        rsa = RSA.importKey(self.local_private)
        cipher = PKCS1_v1_5.new(rsa)
        key = cipher.decrypt(base64.b64decode(response['a']), "出错了")
        logging.debug("远程DES_key:{} b:{} t:{}".format(key.decode(), response['b'], response['t']))
        self.des_key_b = response['b']
        self.des_key_t = response['t']
        self.des_key_a = key.decode()
        return {"s": 0, "b": response['b'], "t": response['t']}

    def decode_flag_103(self, data, flag, isSecure, totalLength, noSecureLength, **kwargs):
        """
        0x67 HTTP_RESPONSE
        :param data:
        :param totalLength:
        :param kwargs:
        :return:
        """

        payload, encryptData = self.unpack(">{}s{}s".format(noSecureLength, totalLength - noSecureLength - 2), data)
        encryptData = self.decrypt_by_des_cbc(data=encryptData)
        headers, encryptBody = encryptData.split(b'\x00', 1)
        body = self.ndug(encryptBody)
        if body.startswith(b'\x4f'):
            result_model = decode_model(body)
            logging.debug("最终生成model:{}".format(result_model))
            return result_model


if __name__ == '__main__':
    from pprint import pprint

    logging.basicConfig(level="DEBUG")

    dp = DPRequest()
    dp.get_key()
    data = {'h': {'User-Agent': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
                  'network-type': 'wifi',
                  'pragma-device': '864394010164947',
                  'pragma-dpid': '3143856292913715455',
                  'pragma-os': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
                  'pragma-unionid': '1bd3f91c3cea40489722048f612868010000000000040575930',
                  'pragma-uuid': 'd4bb88a5-b1c3-46d5-87ed-c9df4ad8faa4'},
            'i': '13713811',
            'm': 'GET',
            'u': 'http://mapi.dianping.com/meishi/selectlist/meishipoilist.api?isfoodcatelocal=false&ganextindex=0&disablerewrite=0&parentcategoryid=10&userid=0&regiontype=0&myacc=-1.0&start=0&mylng=108.13153666666668&mylat=22.000006666666664&categoryid=112&sortid=0&locatecityid=1568&cityid=16'}

    data = dp.make_data(data, flag=0x66)
    connecon = dp.conncon
    connecon.sendall(data)
    res = dp.decode_data(connecon)
    pprint(res)
    logging.basicConfig(level='DEBUG')
    res = decode_model(
        '4f4f314da79d544decb649000000004d742b4e4df10e4ff10e4db2834e4d36e94e4d475e4e4d2610465a4dc06a4f6c524db2835300e96469616e70696e673a2f2f7765623f75726c3d68747470732533412532462532466d2e6469616e70696e672e636f6d2532466d6f62696c6525324673686f7072616e6b2532466368616e6e656c64657461696c253346636974794964253344313625323663617465676f72794964253344313333382532367479706525334431253236736f7274253344706f7073636f72652532366c6f6e6769747564652533442a2532366c617469747564652533442a25323675746d5f736f75726365253344636f5f74656d7025323675746d5f63616d706169676e253344746f706c69737473686f7072616e6b4d475e4e4db0bb4e4d36e95300325b7b2274657874223a22e3808ce6ada6e6b189e7a781e688bfe88f9ce783ade997a8e6a69ce3808de7acac31e5908d227d5d5a4dbc7e5300004d07f2464d365f4e4da69c4e4d73f9530009e7a781e688bfe88f9c4dae5d464ded024e4dd2884e4d07ee49000000004d0996464d14e54e4df4264e4ddc734e4d08654e4d870f4904060a2c4d1de14e4d7217464d881b5300004d835c464dad584e4d8d2941000153000b31333937313232303734394d41db530015e4bb98e58588e7949fe59ca8e68890e983bde697814d29cc5300004d08d9464d579553000ce8a7a3e694bee585ace59bad4da7f44100014fd6df4d037249000000004dee8f53001be591a8e4b880e887b3e591a8e697a50a31323a30302d32313a33304d091b53000ce890a5e4b89ae697b6e997b45a4d134949000000004d134849000000004de58b464d79ca4e4de7e04e4d448549000000004d106549000000004d953e464d30d5530008667269656e645f624d6a4d4100044f6a4d4dee8f530003e88f9c4d630b49000000014d037249000000004d512441001853000fe7949fe88f9ce58c85e7899be8828953000fe79fb3e89b99e783a7e587a4e788aa53000fe88a9de5a3abe78497e68987e8b49d53000fe88a9de5a3abe78497e5a4a7e899be53000fe88a9de5a3abe783a4e99da2e58c8553000fe6a285e985b1e783a4e78caae68e9253001ee58e9ae58887e4b889e69687e9b1bce588bae8baabe68bbce88ab1e89eba530009e5b08fe7be8ae68e9253000fe58fa3e89891e78497e6bb91e899be530015e7a2b3e783a4e99baae88ab1e7899be5b08fe68e9253000ce88289e89fb9e785b2e9b8a1530012e586ace998b4e58a9fe6b5b7e9b29ce99485530018e9a9ace88b8fe9878ce68b89e78497e5a4a7e58583e8b49d530012e586ace998b4e882a5e7899be781abe9948553000fe88aa6e7ac8be883a1e8909de58d9c53000ce7b396e9868be68e92e9aaa853000ce9bb84e98791e899bee7908353000fe9bb91e6a492e783a4e6a182e9b1bc530018e9a9ace88b8fe9878ce785aee789b9e5a4a7e58583e8b49d53000fe88a9de5a3abe7899be8828be68e9253000fe4b889e69687e9b1bce5afbfe58fb853000ce89c9ce588b6e788aae89b9953000fe99baae9b1bce8a5bfe4baace783a753000fe5b9b4e7b395e783a7e9b8a1e7bf855a4f6a4d4dee8f530006e78eafe5a2834d630b49000000004d037249000000014d5124410005530006e997a8e99da2530006e5a4a7e5a082530006e58c85e688bf530009e699afe8a782e4bd8d53000ce9a490e585b7e69186e8aebe5a4f6a4d4dee8f530009e4bbb7e79baee8a1a84d630b49000000004d037249000000014d5124410002530006e88f9ce58d95530006e8b4a6e58d955a4f6a4d4dee8f530006e585a8e983a84d630b49000000014d037249000000014d51244e5a4dcb9a4100004d11394f11394da7064e4d282049000000004db96a5300005a4d54914f54914d297e44403e9a4fa8b4bf904d4b3f53000547434a30324d2b0444405c93be61cffeb05a4d17ba5300004d562d44405c93be61cffeb04dc86a4100014f34024d0372530001314db0bb53003d687474703a2f2f7777772e647066696c652e636f6d2f73632f656c65636f6e6669672f3230313531323032313130333539776966695f6e65772e706e675a4d25a85300025b5d4da8af5300c3e7949fe88f9ce58c85e7899be882892c33397ce79fb3e89b99e783a7e587a4e788aa2c33347ce88a9de5a3abe78497e68987e8b49d2c33347ce88a9de5a3abe78497e5a4a7e899be2c32347ce88a9de5a3abe783a4e99da2e58c852c32337ce6a285e985b1e783a4e78caae68e922c31377ce58e9ae58887e4b889e69687e9b1bce588bae8baabe68bbce88ab1e89eba2c31357ce5b08fe7be8ae68e922c31357ce58fa3e89891e78497e6bb91e899be2c31347ce88289e89fb9e785b2e9b8a12c367c4d72914e4dd8bc4e4d88e8530021e58fa3e591b33a392e3220e78eafe5a2833a392e3220e69c8de58aa13a392e33204da4a45300004dc69e53002ae8b79de59cb0e9938131e58fb7e7babfe9bb84e6b5a6e8b7afe7ab9941e58fa3e6ada5e8a18c3831306d4d89ce4e4d2efc5300004d460d4100004d3835490000000a4d745649000000b84d745749000000b84d745449000000ba4d9e454e4d17454100004dd3a7464d0c1d4e4d31de464d2ab74100004d203f4e4d7d9b490000074d4dac6549000007244d75de4e4d180d44403e9a4fa8b4bf904d9e5c544d0bbe49000000014d454b530009c2a53136342fe4baba4d16064e4d2e2f4e4d255f53002e7b227069634d6f6465223a226d756c7469706963222c2273686f7056696577223a22666f6f645f656e6a6f79227d4d0991464de63f464dbf094e4dbeb749000000324d7697464d65aa4e4da7b449000000104da5d24e4d9702464d0fd54e4de16f464d49f04e4deb1c49000000a44d52714e4d98894fcf404dd885464d991d464d79ca4e4d6d344100034fd6df4d0372490000000a4dee8f53003b687474703a2f2f6d2e6170692e6469616e70696e672e636f6d2f73632f6170695f7265732f7069632f63617465676f72792f666f6f64352e706e674d091b530006e7be8ee9a39f5a4fd6df4d037249000000704dee8f53003c687474703a2f2f6d2e6170692e6469616e70696e672e636f6d2f73632f6170695f7265732f7069632f63617465676f72792f736e61636b352e706e674d091b53000ce5b08fe59083e5bfabe9a4905a4fd6df4d037249000000844dee8f53003d687474703a2f2f6d2e6170692e6469616e70696e672e636f6d2f73632f6170695f7265732f7069632f63617465676f72792f636f66666565352e706e674d091b530009e59296e595a1e58e855a4dd8bc4e5a4d51994100004d041553000b31333937313232303734394dea824e4d4f6f4e4d9ea0490000053a4d45dd464d282049000000004dfee44e4dfa9e5300004dbe8a44403e9a4fa8b4bf904df6094100004d7945490000011d4d022d4f022d4d436f4100014fb2454da5b853001be591a8e4b880e887b3e591a8e697a50a31323a30302d32313a33304dee8f53000ce890a5e4b89ae697b6e997b44da7f44e5a4dd32453000ce59586e688b7e4bfa1e681af5a4de4ac5300277b2274696d65223a22e591a8e4b880e887b3e591a8e697a55c6e31323a30302d32313a3330227d4d1b9449000000004dee8f530003e5928c4d6ee244405c93be61cffeb04d091b4904060a2c4d43e0464d60884100054fb5d14db7164400000000000000004d630b49000000054db2834e4dee8f53000ce59586e5aeb6e4b88ae4bca04dc35653000ce5ae98e696b9e4b88ae4bca04dc6e6530062687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f3533373164623464336539623464653263323234613066363165653138623133253430323830775f323132685f31655f31635f316c25374377617465726d61726b253344304da0da4c00000157ac5624084d861e49237b31784d037249000000004d4d4e53009a687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f3533373164623464336539623464653263323234613066363165653138623133253430373030775f373030685f30655f316c25374377617465726d61726b25334431253236253236722533443125323670253344392532367825334432253236792533443225323672656c6174697665253344312532366f25334432305a4fb5d14db7164400000000000000004d630b49000000054db2834e4dee8f53000ce59586e5aeb6e4b88ae4bca04dc35653000ce5ae98e696b9e4b88ae4bca04dc6e6530062687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f3938316536616633653062333739323839336532623138333665353164373036253430323830775f323132685f31655f31635f316c25374377617465726d61726b253344304da0da4c00000157ac5624084d861e49237b31f54d037249000000004d4d4e53009a687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f3938316536616633653062333739323839336532623138333665353164373036253430373030775f373030685f30655f316c25374377617465726d61726b25334431253236253236722533443125323670253344392532367825334432253236792533443225323672656c6174697665253344312532366f25334432305a4fb5d14db7164400000000000000004d630b49000000054db2834e4dee8f53000ce59586e5aeb6e4b88ae4bca04dc35653000ce5ae98e696b9e4b88ae4bca04dc6e6530062687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f6264336361313162323930643866623837323266363864323862363539343932253430323830775f323132685f31655f31635f316c25374377617465726d61726b253344304da0da4c00000157ac5624084d861e49237b31824d037249000000004d4d4e53009a687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f6264336361313162323930643866623837323266363864323862363539343932253430373030775f373030685f30655f316c25374377617465726d61726b25334431253236253236722533443125323670253344392532367825334432253236792533443225323672656c6174697665253344312532366f25334432305a4fb5d14db7164400000000000000004d630b49000000054db2834e4dee8f53000ce59586e5aeb6e4b88ae4bca04dc35653000ce5ae98e696b9e4b88ae4bca04dc6e6530070687474703a2f2f70302e6d65697475616e2e6e65742f6d736d65726368616e742f37386433626639323034656436663064663835393531663065656665323332343139343330342e6a7067253430323830775f323132685f31655f31635f316c25374377617465726d61726b253344304da0da4c0000015920a2bc084d861e4927b094bd4d037249000000004d4d4e5300a8687474703a2f2f70302e6d65697475616e2e6e65742f6d736d65726368616e742f37386433626639323034656436663064663835393531663065656665323332343139343330342e6a7067253430373030775f373030685f30655f316c25374377617465726d61726b25334431253236253236722533443125323670253344392532367825334432253236792533443225323672656c6174697665253344312532366f25334432305a4fb5d14db7164400000000000000004d630b49000000054db2834e4dee8f53000ce59586e5aeb6e4b88ae4bca04dc35653000ce5ae98e696b9e4b88ae4bca04dc6e6530070687474703a2f2f70302e6d65697475616e2e6e65742f6d736d65726368616e742f37383132366162313336343230323239656133383537663066636233303134323235343834382e6a7067253430323830775f323132685f31655f31635f316c25374377617465726d61726b253344304da0da4c0000015920a5d5004d861e4927b0a1bc4d037249000000004d4d4e5300a8687474703a2f2f70302e6d65697475616e2e6e65742f6d736d65726368616e742f37383132366162313336343230323239656133383537663066636233303134323235343834382e6a7067253430373030775f373030685f30655f316c25374377617465726d61726b25334431253236253236722533443125323670253344392532367825334432253236792533443225323672656c6174697665253344312532366f25334432305a4d99c55300004d94ec530062687474703a2f2f70302e6d65697475616e2e6e65742f7567637069632f3533373164623464336539623464653263323234613066363165653138623133253430333030775f323235685f31655f31635f316c25374377617465726d61726b253344304decbf544d8fd149000000004d52d2464d37a6464d3229464dcf04544d2d04530011e5b1b1e6b5b7e585b3e8b7af3336e58fb74d30e7530003392e334d0c8e4e4d30e5530003392e324d68864400000000000000004d6d9d53000a666f6f645f656e6a6f794da28a4e4d68814400000000000000004d084e4e4d30e4530003392e325a')
    pprint(res)
