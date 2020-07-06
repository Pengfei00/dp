# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:47
"""
from model import BaseModel, add_model


@add_model(0xbe51)
class SmartTagInfo(BaseModel):
    field_map = {
        'a': 'secondCate',
        'b': 'firstCate',
        'c': 'category',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_49148(self):
        """
        0xbffc -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_60922(self):
        """
        0xedfa -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_49368(self):
        """
        0xc0d8 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
