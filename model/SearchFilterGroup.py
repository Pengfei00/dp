# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:14
"""
from model import BaseModel, add_model


@add_model(0xde97)
class SearchFilterGroup(BaseModel):
    field_map = {
        'a': 'label',
        'b': 'itemType',
        'c': 'items',
        'd': 'multiSelectable',
        'e': 'name',
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
        self.result[self.field_map.get('e', 'e')] = self.archive_d_g()

    def j_flag_24925(self):
        """
        0x615d -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_b()

    def j_flag_62362(self):
        """
        0xf39a -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_b_archive_c()

    def j_flag_27399(self):
        """
        0x6b07 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_c()

    def j_flag_35464(self):
        """
        0x8a88 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
