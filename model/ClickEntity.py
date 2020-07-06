# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:39
"""
from model import add_model, BaseModel


@add_model(0x6c52)
class ClickEntity(BaseModel):
    field_map = {
        'a': 'tileId',
        'b': 'icon',
        'c': 'scheme',
        'd': 'subTitle',
        'e': 'title',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_14057(self):
        """
        0x36e9 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_g()

    def j_flag_18270(self):
        """
        0x475e -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_45699(self):
        """
        0xb283 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_45243(self):
        """
        0xb0bb -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_49624(self):
        """
        0xc1d8 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
