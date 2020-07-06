# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 22:01
"""
from model import BaseModel, add_model


@add_model(0x3402)
class UnClickEntity(BaseModel):
    field_map = {
        'a': 'icon',
        'b': 'type',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_882(self):
        """
        0x372 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_45243(self):
        """
        0xb0bb -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
