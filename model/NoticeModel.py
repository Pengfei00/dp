# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:57
"""
from model import BaseModel, add_model


@add_model(0x9aa6)
class NoticeModel(BaseModel):
    field_map = {
        'a': 'labelInfo',
        'b': 'view',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_14994(self):
        """
        0x3a92 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_a_archive_c()

    def j_flag_26115(self):
        """
        0x6603 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_a_archive_c()
