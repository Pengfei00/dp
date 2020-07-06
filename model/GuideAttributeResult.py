# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:17
"""
from model import BaseModel, add_model


@add_model(0x31b2)
class GuideAttributeResult(BaseModel):
    field_map = {
        'a': 'guideAttributeList',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_32128(self):
        """
        0x7d80 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_b_archive_c()
