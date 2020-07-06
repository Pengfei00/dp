# -*- coding:utf-8 -*-

"""
@author: Wnstar
@time: 2017/12/14
"""
from __future__ import unicode_literals
from model import add_model, BaseModel


@add_model(0xf7e3)
class ReviewAbstract(BaseModel):
    field_map = {
        'a': 'tagId',
        'b': 'hotelLabelId',
        'c': 'rankType',
        'd': 'count',
        'e': 'affection',
        'f': 'name',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_g()

    def j_flag_16997(self):
        """
        0x4265 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_c()

    def j_flag_25355(self):
        """
        0x630b -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_c()

    def j_flag_44731(self):
        """
        0xaebb -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_c()

    def j_flag_10529(self):
        """
        0x2921 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_c()

    def j_flag_19653(self):
        """
        0x4cc5 -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_c()
