# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:39
"""
from model import add_model, BaseModel


@add_model(0xd6df)
class Pair(BaseModel):
    field_map = {
        'a': 'parentID',
        'b': 'iD',
        'c': 'name',
        'd': 'type',
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
        self.result[self.field_map.get('d', 'd')] = self.archive_d_c()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_2331(self):
        """
        0x91b -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_47744(self):
        """
        0xba80 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
