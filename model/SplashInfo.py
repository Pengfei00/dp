# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 23:55
"""
from model import BaseModel, add_model


@add_model(0xe9c0)
class SplashInfo(BaseModel):
    field_map = {
        'a': 'templateUrl',
        'b': 'data',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_25578(self):
        """
        0x63ea -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_b_archive_c()

    def j_flag_53905(self):
        """
        0xd291 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
