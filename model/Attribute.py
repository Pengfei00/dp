# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 22:06
"""
from model import BaseModel, add_model


@add_model(0xb245)
class Attribute(BaseModel):
    field_map = {
        'a': 'extra',
        'b': 'value',
        'c': 'name',
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
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_42424(self):
        """
        0xa5b8 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_42996(self):
        """
        0xa7f4 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
