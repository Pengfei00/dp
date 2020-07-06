# -*- coding:utf-8 -*-

"""
@author: Wnstar
@time: 2017/12/14
"""
from __future__ import unicode_literals
from model import add_model, BaseModel

"""
点评
"""


@add_model(0x7fad)
class ShopReviewFeedList(BaseModel):
    field_map = {
        'a': 'dishTitleCount',
        'b': 'dishTitle',
        'c': 'bottomTitle',
        'd': 'topTitle',
        'e': 'notice',
        'f': 'reviewAbstractList',
        'g': 'list',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_11655(self):
        """
        0x2d87 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('as', 'as')] = self.archive_d_g()

    def j_flag_42085(self):
        """
        0xa465 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('ar', 'ar')] = self.archive_d_g()

    def j_flag_22275(self):
        """
        0x5703 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('aq', 'aq')] = self.archive_d_c()

    def j_flag_3851(self):
        """
        0xf0b -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('ap', 'ap')] = self.archive_d_b()

    def j_flag_43620(self):
        """
        0xaa64 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('ao', 'ao')] = self.archive_d_c()

    def j_flag_6013(self):
        """
        0x177d -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('an', 'an')] = self.archive_d_c()

    def j_flag_9370(self):
        """
        0x249a -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_b_archive_c()

    def j_flag_33146(self):
        """
        0x817a -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_b_archive_c()

    def j_flag_2452(self):
        """
        0x994 -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_g()

    def j_flag_43909(self):
        """
        0xab85 -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_56496(self):
        """
        0xdcb0 -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_50048(self):
        """
        0xc380 -> :sswitch_c
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_15647(self):
        """
        0x3d1f -> :sswitch_d
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
