# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 22:04
"""
from model import BaseModel, add_model


@add_model(0x22d)
class ShopExtraInfo(BaseModel):
    field_map = {
        'a': 'shopExtraInfosTitle',
        'b': 'shopExtraInfos',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_17263(self):
        """
        0x436f -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_b_archive_c()

    def j_flag_54052(self):
        """
        0xd324 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
