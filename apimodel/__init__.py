# -*- coding:utf-8 -*-

"""
@author: Wnstar
@time: 2017/12/15
"""
from __future__ import unicode_literals
import random
import uuid

from collections import UserDict

# {'h': {'User-Agent': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
#   'network-type': 'wifi',
#   'pragma-device': '864394010164947',
#   'pragma-dpid': '3143856292913715455',
#   'pragma-os': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
#   'pragma-unionid': '1bd3f91c3cea40489722048f612868010000000000040575930',
#   'pragma-uuid': 'd4bb88a5-b1c3-46d5-87ed-c9df4ad8faa4'},
#  'i': '13713803',
#  'm': 'GET',
#  'u': 'http://mapi.dianping.com/meishi/selectlist/meishipoilist.api?isfoodcatelocal=false&ganextindex=0&disablerewrite=0&parentcategoryid=-1&userid=0&myacc=-1.0&start=0&mylng=108.13153666666668&mylat=22.000006666666664&categoryid=10&locatecityid=1568&cityid=16'}

#
# {'h': {'User-Agent': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
#   'network-type': 'wifi',
#   'pragma-device': '864394010164947',
#   'pragma-dpid': '3143856292913715455',
#   'pragma-os': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
#   'pragma-unionid': '1bd3f91c3cea40489722048f612868010000000000040575930',
#   'pragma-uuid': 'd4bb88a5-b1c3-46d5-87ed-c9df4ad8faa4'},
#  'i': '173664373',
#  'm': 'GET',
#  'u': 'http://mapi.dianping.com/meishi/selectlist/meishipoilist.api?isfoodcatelocal=false&ganextindex=25&lastpageshopids=69858200%2C91669175%2C5480139%2C18989038%2C92519558%2C8977386%2C549463%2C92915194%2C18332562%2C57420223&disablerewrite=0&parentcategoryid=-1&userid=0&regiontype=0&myacc=-1.0&start=25&mylng=108.13153666666668&mylat=22.000006666666664&categoryid=10&sortid=0&locatecityid=1568&cityid=16'}
#
# {'h': {'Accept': 'application/json;charset=UTF-8',
#   'Content-Encoding': 'gzip',
#   'Content-Type': 'application/json;charset=UTF-8',
#   'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; HTC D816w Build/KOT49H)'},
#  'i': '173664374',
#  'm': 'GET',
# 'u': 'http://api.meishi.meituan.com/meishi/filter/v1/dp/smarttips?hasGroup=true&client=android&plat_source=dp&dpid=3143856292913715455&utm_source=om_sd_baidu_cpdnew&unionid=1bd3f91c3cea40489722048f612868010000000000040575930&cityId=16&cateId=10&mypos=22.000006666666664%2C108.13153666666668&stationId=0&lineId=0&areaId=0&offset=25&reqId=de486b4e-1f83-4c36-a5c9-250705963b4c&utm_medium=android&utm_term=9702&version_name=9.7.3&utm_content=864394010164947&utm_campaign=utm_campaign&ci=16&uuid=d4bb88a5-b1c3-46d5-87ed-c9df4ad8faa4&msid=9e4cd909-945b-4c04-afc0-ce99313dadbf&app_platform=dp&dpch=om_sd_baidu_cpdnew&userid=-1&platform=4&partner=123&__skck=6a375bce8c66a0dc293860dfa83833ef&__skts=1513492918868&__skua=598842aced50d3d3eeafe5c9edd17517&__skno=3f0f02c6-5c43-42d3-9020-12b2f0d98176&__skcy=qBPbdf1DZuySDCwCdcddA%2B60%2BN0%3D'}
#
# {'h': {'User-Agent': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
#   'network-type': 'wifi',
#   'pragma-device': '864394010164947',
#   'pragma-dpid': '3143856292913715455',
#   'pragma-os': 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)',
#   'pragma-unionid': '1bd3f91c3cea40489722048f612868010000000000040575930',
#   'pragma-uuid': 'd4bb88a5-b1c3-46d5-87ed-c9df4ad8faa4'},
#  'i': '173664377',
#  'm': 'GET',
#  'u': 'http://mapi.dianping.com/meishi/selectlist/meishipoilist.api?isfoodcatelocal=false&ganextindex=50&lastpageshopids=90479838%2C69173535%2C4742010%2C21015721%2C93956084%2C76973417%2C69795601%2C5685162%2C93550351%2C90575493&disablerewrite=0&parentcategoryid=-1&userid=0&regiontype=0&myacc=-1.0&start=50&mylng=108.13153666666668&mylat=22.000006666666664&categoryid=10&sortid=0&locatecityid=1568&cityid=16'}


User_Agent = 'MApi 1.1 (com.dianping.v1 9.7.3 om_sd_baidu_cpdnew HTC_D816w; Android 4.4.2)'
Network_type = 'wifi'
Pragma_Device = str(random.randint(164394010164947, 964394010164947))
Pragma_Dpid = str(random.randint(1143856292913715455, 9143856292913715455))
Pragma_Os = User_Agent
Pragma_Unionid = '1bd3f91c3cea40489722048f612868010000000000040575930',
Pragma_Uuid = uuid.uuid4()


class BaseApi(object):
    def __init__(self, index, data):
        self.headers = {'User-Agent': User_Agent,
                        'network-type': Network_type,
                        'pragma-device': Network_type,
                        'pragma-dpid': Pragma_Dpid,
                        'pragma-os': Pragma_Os,
                        'pragma-unionid': Pragma_Unionid,
                        'pragma-uuid': Pragma_Uuid}
        self.i = index
