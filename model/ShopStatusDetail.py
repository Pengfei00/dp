# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 22:00
"""
from model import BaseModel, add_model


@add_model(0x1139)
class ShopStatusDetail(BaseModel):
    field_map = {
        'a': 'clickUrl',
        'b': 'status',
        'c': 'text',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_47466(self):
        """
        0xb96a -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_10272(self):
        """
        0x2820 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_c()

    def j_flag_42758(self):
        """
        0xa706 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
