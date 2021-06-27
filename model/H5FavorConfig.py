
# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:39
"""
from model import add_model, BaseModel


@add_model(0x63a5)
class H5FavorConfig(BaseModel):
    field_map = {

    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_10554(self):
        """
        0x293a -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_n()

    def j_flag_53848(self):
        """
        0xd258 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_n()

