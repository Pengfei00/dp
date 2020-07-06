# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 23:57
"""
from model import BaseModel, add_model


@add_model(0x8578)
class Splash(BaseModel):
    field_map = {
        'a': 'feedBack',
        'b': 'requestTime',
        'c': 'splashId',
        'd': 'startTime',
        'e': 'endTime',
        'f': 'showTime',
        'g': 'city',
        'h': 'adUrl',
        'i': 'clickUrl',
        'j': 'viewUrl',
        'k': 'costType',
        'l': 'resourceType',
        'm': 'resourceUrl',
        'n': 'showNumber',
        'o': 'bg',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_2149(self):
        """
        0x865 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('o', 'o')] = self.archive_d_g()

    def j_flag_4548(self):
        """
        0x11c4 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('n', 'n')] = self.archive_d_c()

    def j_flag_41630(self):
        """
        0xa29e -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('m', 'm')] = self.archive_d_g()

    def j_flag_38506(self):
        """
        0x966a -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('l', 'l')] = self.archive_d_c()

    def j_flag_33357(self):
        """
        0x824d -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('k', 'k')] = self.archive_d_c()

    def j_flag_4641(self):
        """
        0x1221 -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_g()

    def j_flag_42758(self):
        """
        0xa706 -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_g()

    def j_flag_47598(self):
        """
        0xb9ee -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_3499(self):
        """
        0xdab -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_g()

    def j_flag_53282(self):
        """
        0xd022 -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_c()

    def j_flag_324(self):
        """
        0x144 -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_g()

    def j_flag_21160(self):
        """
        0x52a8 -> :sswitch_c
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_2705(self):
        """
        0xa91 -> :sswitch_d
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_9770(self):
        """
        0x262a -> :sswitch_e
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_d()

    def j_flag_15268(self):
        """
        0x3ba4 -> :sswitch_f
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
