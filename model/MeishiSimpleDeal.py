# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:29
"""
from model import BaseModel, add_model


@add_model(0x73b2)
class MeishiSimpleDeal(BaseModel):
    field_map = {
        'a': 'dealType',
        'b': 'dealTitle',
        'c': 'tagInfo',
        'd': 'subDealTitle',
        'e': 'iconUrl',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_61168(self):
        """
        0xeef0 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_a_archive_c()

    def j_flag_58004(self):
        """
        0xe294 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_54679(self):
        """
        0xd597 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_b_archive_c()

    def j_flag_8049(self):
        """
        0x1f71 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_a_archive_c()

    def j_flag_28579(self):
        """
        0x6fa3 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_c()
