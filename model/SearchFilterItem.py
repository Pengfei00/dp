# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:16
"""
from model import BaseModel, add_model


@add_model(0x2087)
class SearchFilterItem(BaseModel):
    field_map = {
        'a': 'desc',
        'b': 'selected',
        'c': 'type',
        'd': 'name',
        'e': 'iD',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_2331(self):
        """
        0x91b -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_g()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_882(self):
        """
        0x372 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_c()

    def j_flag_7259(self):
        """
        0x1c5b -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_b()

    def j_flag_29329(self):
        """
        0x7291 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
