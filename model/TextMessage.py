# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:30
"""
from model import BaseModel, add_model


@add_model(0x57be)
class TextMessage(BaseModel):
    field_map = {
        'a': 'backgroundColor',
        'b': 'color',
        'c': 'content',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_3278(self):
        """
        0xcce -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_10948(self):
        """
        0x2ac4 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_47714(self):
        """
        0xba62 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
