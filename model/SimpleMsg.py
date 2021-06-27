# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/13 21:56
"""

from model import add_model, BaseModel


# todo xiugai


@add_model(0x909d)
class SimpleMsg(BaseModel):
    field_map = {
        'k': 'Data',
        'j': 'StatusCode',
        'i': 'Flag',
        'h': 'Icon',
        'g': 'Content',
        'f': 'Title',
        'e': 'ReturnID',
        'd': 'ErrorCode',
        'c': 'ErrorMsg',
        'b': 'IsPresent',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_b()

    def j_flag_141(self):
        """
        0x8d -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_c()

    def j_flag_14057(self):
        """
        0x36e9 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_g()

    def j_flag_22454(self):
        """
        0x57b6 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_g()

    def j_flag_45243(self):
        """
        0xb0bb -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_c()

    def j_flag_29613(self):
        """
        0x73ad -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_c()

    def j_flag_25578(self):
        """
        0x63ea -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('k', 'k')] = self.archive_d_g()

    def j_flag_29544(self):
        """
        0x7368 -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_17659(self):
        """
        0x44fb -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_c()

    def j_flag_61413(self):
        """
        0xefe5 -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_c()
