# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 21:58
"""
from model import BaseModel, add_model


@add_model(0x6a4d)
class ShopPhotoCategory(BaseModel):
    field_map = {
        'a': 'count',
        'b': 'name',
        'c': 'type',
        'd': 'subCategoryList',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_20772(self):
        """
        0x5124 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_n()

    def j_flag_882(self):
        """
        0x372 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_c()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_25355(self):
        """
        0x630b -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_c()
