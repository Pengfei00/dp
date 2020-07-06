# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:32
"""
from model import BaseModel, add_model


@add_model(0xfda9)
class ShopDisplayTag(BaseModel):
    field_map = {
        'a': 'tagUrl',
        'b': 'bizId',
        'c': 'textType',
        'd': 'iconAlignType',
        'e': 'priority',
        'f': 'alignType',
        'g': 'cornerRadius',
        'h': 'backgroundColor',
        'i': 'fontSize',
        'j': 'iconTextSpacing',
        'k': 'iconHeight',
        'l': 'iconWidth',
        'm': 'borderColor',
        'n': 'textColor',
        'o': 'icon',
        'p': 'type',
        'q': 'text',
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
        self.result[self.field_map.get('q', 'q')] = self.archive_d_g()

    def j_flag_882(self):
        """
        0x372 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('p', 'p')] = self.archive_d_c()

    def j_flag_45243(self):
        """
        0xb0bb -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('o', 'o')] = self.archive_d_g()

    def j_flag_30235(self):
        """
        0x761b -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('n', 'n')] = self.archive_d_g()

    def j_flag_40968(self):
        """
        0xa008 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('m', 'm')] = self.archive_d_g()

    def j_flag_8369(self):
        """
        0x20b1 -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('l', 'l')] = self.archive_d_e()

    def j_flag_53941(self):
        """
        0xd2b5 -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('k', 'k')] = self.archive_d_e()

    def j_flag_11544(self):
        """
        0x2d18 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_e()

    def j_flag_7349(self):
        """
        0x1cb5 -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_e()

    def j_flag_49151(self):
        """
        0xbfff -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_26611(self):
        """
        0x67f3 -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_e()

    def j_flag_20345(self):
        """
        0x4f79 -> :sswitch_c
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_c()

    def j_flag_25510(self):
        """
        0x63a6 -> :sswitch_d
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_c()

    def j_flag_65480(self):
        """
        0xffc8 -> :sswitch_e
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_c()

    def j_flag_34351(self):
        """
        0x862f -> :sswitch_f
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_c()

    def j_flag_40637(self):
        """
        0x9ebd -> :sswitch_10
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_36683(self):
        """
        0x8f4b -> :sswitch_11
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
