# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:31
"""
from model import BaseModel, add_model


@add_model(0xadda)
class SearchIconItem(BaseModel):
    field_map = {
        'a': 'height',
        'b': 'width',
        'c': 'url',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_19790(self):
        """
        0x4d4e -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_14685(self):
        """
        0x395d -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_e()

    def j_flag_64986(self):
        """
        0xfdda -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_e()
