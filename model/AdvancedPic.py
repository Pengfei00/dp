# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/17 22:07
"""
from model import BaseModel, add_model


@add_model(0xb5d1)
class AdvancedPic(BaseModel):
    field_map = {
        'a': 'type',
        'b': 'picId',
        'c': 'price',
        'd': 'uploader',
        'e': 'count',
        'f': 'scheme',
        'g': 'uploadTime',
        'h': 'name',
        'i': 'url',
        'j': 'thumbUrl',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_50918(self):
        """
        0xc6e6 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_g()

    def j_flag_19790(self):
        """
        0x4d4e -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_g()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_41178(self):
        """
        0xa0da -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_d()

    def j_flag_45699(self):
        """
        0xb283 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_g()

    def j_flag_25355(self):
        """
        0x630b -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_c()

    def j_flag_50006(self):
        """
        0xc356 -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_46870(self):
        """
        0xb716 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_e()

    def j_flag_34334(self):
        """
        0x861e -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_c()

    def j_flag_882(self):
        """
        0x372 -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_c()
