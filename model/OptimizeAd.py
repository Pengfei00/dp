# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 0:36
"""
from model import add_model, BaseModel


@add_model(0x3111)
class OptimizeAd(BaseModel):
    field_map = {
        'a': 'adShops',
        'b': 'jumpUrl',
        'c': 'position',
        'd': 'title',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_9420(self):
        """
        0x24cc -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_46523(self):
        """
        0xb5bb -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_c()

    def j_flag_30542(self):
        """
        0x774e -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_8057(self):
        """
        0x1f79 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_b_archive_c()
