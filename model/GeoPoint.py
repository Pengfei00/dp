# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:36
"""
from model import BaseModel, add_model


@add_model(0x5491)
class GeoPoint(BaseModel):
    field_map = {
        'a': 'lat',
        'b': 'lng',
        'c': 'coordType',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_19263(self):
        """
        0x4b3f -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_11012(self):
        """
        0x2b04 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_e()

    def j_flag_10622(self):
        """
        0x297e -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_e()
