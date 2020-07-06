# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:56
"""
from model import BaseModel, add_model


@add_model(0x35ce)
class BannerRecord(BaseModel):
    field_map = {
        'a': 'title',
        'b': 'adLabel',
        'c': 'bannerType',
        'd': 'bannerId',
        'e': 'picUrl',
        'f': 'clickUrl',
        'g': 'monitorImpUrl',
        'h': 'monitorClickUrl',
        'i': 'feedback',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_47061(self):
        """
        0xb7d5 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_g()

    def j_flag_9222(self):
        """
        0x2406 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_29977(self):
        """
        0x7519 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_g()

    def j_flag_42758(self):
        """
        0xa706 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_g()

    def j_flag_11740(self):
        """
        0x2ddc -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_g()

    def j_flag_17595(self):
        """
        0x44bb -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_c()

    def j_flag_53749(self):
        """
        0xd1f5 -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_c()

    def j_flag_9479(self):
        """
        0x2507 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_14057(self):
        """
        0x36e9 -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
