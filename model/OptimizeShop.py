# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 1:50
"""

from model import add_model, BaseModel


# todo xiugai

@add_model(0xf7fe)
class OptimizeShop(BaseModel):
    field_map = {
        'a': 'feedback',
        'b': 'iconUrl',
        'c': 'defaultPic',
        'd': 'title',
        'e': 'id',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_3355(self):
        """
        0xd1b -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_c()

    def j_flag_9420(self):
        """
        0x24cc -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_g()

    def j_flag_2042(self):
        """
        0x7fa -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_62363(self):
        """
        0xf39b -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_g()

    def j_flag_7952(self):
        """
        0x1f10 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
