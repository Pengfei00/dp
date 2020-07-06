# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 20:10
"""
from model import add_model, BaseModel


@add_model(0x27c3)
class Category(BaseModel):
    field_map = {
        'a': 'link',
        'b': 'label',
        'c': 'isHotCategory',
        'd': 'schema',
        'e': 'iD',
        'f': 'name',
        'g': 'parentID',
        'h': 'favIcon',
        'i': 'distance',
        'j': 'searchPara',
        'k': 'highlight',
        'l': 'enName',
        'm': 'parentEnName',
        'n': 'count',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_25355(self):
        """
        0x630b -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('n', 'n')] = self.archive_d_c()

    def j_flag_4315(self):
        """
        0x10db -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('m', 'm')] = self.archive_d_g()

    def j_flag_4357(self):
        """
        0x1105 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('l', 'l')] = self.archive_d_g()

    def j_flag_57923(self):
        """
        0xe243 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('k', 'k')] = self.archive_d_b()

    def j_flag_18879(self):
        """
        0x49bf -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_g()

    def j_flag_58654(self):
        """
        0xe51e -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_c()

    def j_flag_60687(self):
        """
        0xed0f -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_47744(self):
        """
        0xba80 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_c()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_g()

    def j_flag_2331(self):
        """
        0x91b -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_c()

    def j_flag_45703(self):
        """
        0xb287 -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_40690(self):
        """
        0x9ef2 -> :sswitch_c
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_b()

    def j_flag_35464(self):
        """
        0x8a88 -> :sswitch_d
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_c()

    def j_flag_9278(self):
        """
        0x243e -> :sswitch_e
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
