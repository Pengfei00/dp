# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 22:03
"""
from model import BaseModel, add_model


@add_model(0xcf40)
class TouristInfo(BaseModel):
    field_map = {
        'a': 'recommends',
        'b': 'recommendIcon',
        'c': 'searchCategory',
        'd': 'newPage',
        'e': 'isHotel',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_55429(self):
        """
        0xd885 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_b()

    def j_flag_39197(self):
        """
        0x991d -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_b()

    def j_flag_27956(self):
        """
        0x6d34 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_b_archive_c()

    def j_flag_55484(self):
        """
        0xd8bc -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_31178(self):
        """
        0x79ca -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
