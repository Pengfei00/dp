# -*- coding:utf-8 -*-

"""
@author: Wnstar
@time: 2017/12/14
"""
from __future__ import unicode_literals
from model import add_model, BaseModel


@add_model(0xeac0)
class ShopCover(BaseModel):
    field_map = {
        'a': 'nextUrl',
        'b': 'backgroundPic',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_8797(self):
        """
        0x225d -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_38763(self):
        """
        0x976b -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
