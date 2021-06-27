# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/13 2:33
"""
import struct
import os
from io import BytesIO
import logging

flag_model_map = {}


class BaseModel:
    field_map = {}

    def __init__(self, data):
        self.result = {}
        if isinstance(data, BytesIO):
            self.data = data
            self.raw_data = data
        else:
            self.raw_data = data
            self.data = BytesIO(data)

    def unpack(self, fmt, stream):
        size = struct.calcsize(fmt)
        buf = stream.read(size)
        try:
            return struct.unpack(fmt, buf)
        except struct.error as e:
            logging.error("数据不全:{}".format(buf))

    def main(self):
        self.result = self.archive_d_a_archive_c()
        return self.result

    def decode(self):
        while True:
            j_flag = self.archive_d_j()
            if j_flag < 1:
                break
            j_flag_func_name = 'j_flag_{}'.format(j_flag)
            if hasattr(self, j_flag_func_name):
                getattr(self, j_flag_func_name)()
            else:
                try:
                    self.archive_d_i()
                except ValueError as e:
                    logging.error("数据错误不解析了 j_flag:{} 当前model:{}".format(j_flag, self.__class__))
                    raise e

    def archive_d_b(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x54:
            data = 0x1
        elif flag in [0x46, 0x4e]:
            data = 0x0
        else:
            logging.error("archive_d_b抛错:unable to read boolean")
            raise ValueError()
        logging.info("找到bool:{}".format(data))
        return data

    def archive_d_c(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x49:
            data, = self.unpack(">i", self.data)
        elif flag == 0x4e:
            data = 0x00
        else:
            logging.error("archive_d_c抛错")
            raise ValueError()
        logging.info("找到int:{}".format(data))
        return data

    def archive_d_d(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x4c:
            data, = self.unpack(">q", self.data)
        elif flag == 0x4e:
            data = 0x0
        else:
            logging.error("archive_d_d抛错")
            raise ValueError()
        logging.info("archive_d_d找到string:{}".format(data))
        return data

    def archive_d_j(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x4d:
            data, = self.unpack(">h", self.data)
            data &= 0xffff
        elif flag == 0x5a:
            data = 0x00
        else:
            logging.error("archive_d_j抛错")
            raise ValueError()
        logging.info("当前model{}".format(self.__class__))
        return data

    def archive_d_e(self):
        flag, = self.unpack(">b", self.data)

        if flag == 0x44:
            data, = self.unpack(">d", self.data)
        elif flag == 0x4e:
            data = 0x0
        else:
            logging.error("archive_d_e抛错")
            raise ValueError()
        logging.info("当前model{}".format(self.__class__))
        return data

    def archive_d_g(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x53:
            length, = self.unpack(">h", self.data)
            length = 0xffff & length
            data, = self.unpack(">{}s".format(length), self.data)
        elif flag == 0x4e:
            data = b""
        elif flag == 0x42:
            length, = self.unpack(">i", self.data)
            j = (int(length / 0x1000) + 0x1) * 0x1000
            data, = self.unpack(">{}s".format(length), self.data)
        else:
            logging.error("archive_d_g抛错")
            raise ValueError()

        logging.info("找到string:{}".format(data.decode()))
        return data.decode()

    def archive_d_n(self):
        data = []
        flag, = self.unpack(">b", self.data)
        if flag == 0x4e:
            data = [""]
        elif flag == 0x41:
            length, = self.unpack(">h", self.data)
            length = 0xffff & length
            for i in range(length):
                data.append(self.archive_d_g())
        else:
            logging.error("archive_d_n抛错")
            raise ValueError()
        logging.info("找到string:{}".format(data))
        return data

    def archive_d_i(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x41:
            length, = self.unpack(">h", self.data)
            length = length & 0xffff
            for i in range(length):
                self.archive_d_i()
        elif flag == 0x44:
            self.unpack(">d", self.data)
        elif flag == 0x49:
            self.unpack(">i", self.data)
        elif flag == 0x4c:
            self.unpack(">q", self.data)
        elif flag == 0x4f:
            self.unpack(">h", self.data)
            while self.archive_d_j() > 0:
                self.archive_d_i()
        elif flag == 0x53:
            position, = self.unpack(">h", self.data)
            position = (position & 0xffff) + self.data.tell()
            self.data.seek(position)
        elif flag == 0x55:
            self.unpack(">i", self.data)
        elif flag in [0x46, 0x4e, 0x54, ]:
            pass
        elif flag in [0x42, 0x43, 0x45, 0x47, 0x48, 0x4a, 0x4b, 0x4d, 0x50, 0x51, 0x52]:
            raise ValueError("unable to skip object:")

    def archive_d_a_archive_c(self):
        flag, = self.unpack(">b", self.data)
        if flag == 0x4e:
            logging.info("创建了一个空对象")
            return {}
        elif flag == 0x4f:
            data, = self.unpack(">h", self.data)
            data &= 0xffff
            model_class = flag_model_map.get(data, None)
            if model_class:
                model_instance = model_class(self.data)
                model_instance.decode()
                return model_instance.result
            else:
                logging.error("archive_d_a_archive_c未找到此model：{}".format(hex(data)))
                raise ValueError()
        else:
            logging.error("archive_d_a_archive_c抛错")
            raise ValueError()

    def archive_d_b_archive_c(self):
        result = []
        flag, = self.unpack(">b", self.data)
        if flag == 0x4e:
            logging.info("创建空对象")
            return []
        elif flag == 0x41:
            length, = self.unpack(">h", self.data)
            length = 0xffff & length
            for i in range(length):
                data = self.archive_d_a_archive_c()
                logging.info("创建了一个对象:{}".format(data))
                result.append(data)
            return result
        else:
            logging.error("抛错")
            raise ValueError()


def add_model(flag):
    def wrapper(cls):
        if flag_model_map.get(flag):
            raise ValueError("model已存在:{}".format(flag))
        flag_model_map[flag] = cls
        return cls

    return wrapper


def decode_model(data):
    """

    :param data:
    :return: dict
    """
    if not isinstance(data, bytes):
        data = bytes.fromhex(data)
    logging.debug("需要解密的body:{}".format(data.hex()))
    basemodel = BaseModel(data)
    basemodel.main()
    result = basemodel.result
    return result


def import_all_model():
    all_list = os.listdir(os.path.dirname(__file__))
    for i in all_list:
        if "__" not in i and ".py" in i:
            __import__("model." + i.replace(".py", ""))


import_all_model()
