# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:39
"""
from model import BaseModel, add_model


@add_model(0x6650)
class CompositeMessage(BaseModel):
    field_map = {
        'a': 'text',
        'b': 'icon',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_15432(self):
        """
        0x3c48 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_17691(self):
        """
        0x451b -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_a_archive_c()
