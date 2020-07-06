# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:39
"""
from model import add_model, BaseModel


@add_model(0xf10e)
class TakeOrder(BaseModel):
    field_map = {
        'a': 'scheme',
        'b': 'subTitle',
        'c': 'title',
        'd': 'canOrder',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_9744(self):
        """
        0x2610 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_b()

    def j_flag_14057(self):
        """
        0x36e9 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_18270(self):
        """
        0x475e -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_45699(self):
        """
        0xb283 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
