# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:58
"""
from model import BaseModel, add_model


@add_model(0x163)
class FilterNavi(BaseModel):
    field_map = {
        'a': 'filterGroups',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_8146(self):
        """
        0x1fd2 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_b_archive_c()
