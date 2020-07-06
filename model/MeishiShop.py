# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 22:26
"""
from model import BaseModel, add_model


@add_model(0xc5bc)
class MeishiShop(BaseModel):
    field_map = {
        'a': 'isNewShopProtect',
        'b': 'picNewExtraRightBottom',
        'c': 'picNewExtraLeft',
        'd': 'shopNewDeals',
        'e': 'stateNewInfos',
        'f': 'picExtraLeft',
        'g': 'notices',
        'h': 'reviewCountStr',
        'i': 'paymentTags',
        'j': 'smartTags',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_18834(self):
        """
        0x4992 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('dy', 'dy')] = self.archive_d_c()

    def j_flag_60607(self):
        """
        0xecbf -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('dx', 'dx')] = self.archive_d_b()

    def j_flag_8255(self):
        """
        0x203f -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('dw', 'dw')] = self.archive_d_g()

    def j_flag_31045(self):
        """
        0x7945 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('dv', 'dv')] = self.archive_d_c()

    def j_flag_17933(self):
        """
        0x460d -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('du', 'du')] = self.archive_d_b_archive_c()

    def j_flag_2449(self):
        """
        0x991 -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('dt', 'dt')] = self.archive_d_b()

    def j_flag_27092(self):
        """
        0x69d4 -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('ds', 'ds')] = self.archive_d_c()

    def j_flag_30216(self):
        """
        0x7608 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('dr', 'dr')] = self.archive_d_b_archive_c()

    def j_flag_40517(self):
        """
        0x9e45 -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('dq', 'dq')] = self.archive_d_a_archive_c()

    def j_flag_53999(self):
        """
        0xd2ef -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('dp', 'dp')] = self.archive_d_b()

    def j_flag_21105(self):
        """
        0x5271 -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('do', 'do')] = self.archive_d_g()

    def j_flag_58540(self):
        """
        0xe4ac -> :sswitch_c
        :return:
        """
        self.result[self.field_map.get('dn', 'dn')] = self.archive_d_g()

    def j_flag_12766(self):
        """
        0x31de -> :sswitch_d
        :return:
        """
        self.result[self.field_map.get('dm', 'dm')] = self.archive_d_b()

    def j_flag_40540(self):
        """
        0x9e5c -> :sswitch_e
        :return:
        """
        self.result[self.field_map.get('dl', 'dl')] = self.archive_d_b()

    def j_flag_50613(self):
        """
        0xc5b5 -> :sswitch_f
        :return:
        """
        self.result[self.field_map.get('dk', 'dk')] = self.archive_d_c()

    def j_flag_53896(self):
        """
        0xd288 -> :sswitch_10
        :return:
        """
        self.result[self.field_map.get('dj', 'dj')] = self.archive_d_a_archive_c()

    def j_flag_28386(self):
        """
        0x6ee2 -> :sswitch_11
        :return:
        """
        self.result[self.field_map.get('di', 'di')] = self.archive_d_e()

    def j_flag_6157(self):
        """
        0x180d -> :sswitch_12
        :return:
        """
        self.result[self.field_map.get('dh', 'dh')] = self.archive_d_e()

    def j_flag_2265(self):
        """
        0x8d9 -> :sswitch_13
        :return:
        """
        self.result[self.field_map.get('dg', 'dg')] = self.archive_d_b()

    def j_flag_35171(self):
        """
        0x8963 -> :sswitch_14
        :return:
        """
        self.result[self.field_map.get('df', 'df')] = self.archive_d_g()

    def j_flag_26026(self):
        """
        0x65aa -> :sswitch_15
        :return:
        """
        self.result[self.field_map.get('de', 'de')] = self.archive_d_b_archive_c()

    def j_flag_12519(self):
        """
        0x30e7 -> :sswitch_16
        :return:
        """
        self.result[self.field_map.get('dd', 'dd')] = self.archive_d_g()

    def j_flag_12516(self):
        """
        0x30e4 -> :sswitch_17
        :return:
        """
        self.result[self.field_map.get('dc', 'dc')] = self.archive_d_g()

    def j_flag_12517(self):
        """
        0x30e5 -> :sswitch_18
        :return:
        """
        self.result[self.field_map.get('db', 'db')] = self.archive_d_g()

    def j_flag_14246(self):
        """
        0x37a6 -> :sswitch_19
        :return:
        """
        self.result[self.field_map.get('da', 'da')] = self.archive_d_b()

    def j_flag_4053(self):
        """
        0xfd5 -> :sswitch_1a
        :return:
        """
        self.result[self.field_map.get('cZ', 'cZ')] = self.archive_d_g()

    def j_flag_2034(self):
        """
        0x7f2 -> :sswitch_1b
        :return:
        """
        self.result[self.field_map.get('cY', 'cY')] = self.archive_d_b()

    def j_flag_33628(self):
        """
        0x835c -> :sswitch_1c
        :return:
        """
        self.result[self.field_map.get('cX', 'cX')] = self.archive_d_b()

    def j_flag_44637(self):
        """
        0xae5d -> :sswitch_1d
        :return:
        """
        self.result[self.field_map.get('cW', 'cW')] = self.archive_d_b()

    def j_flag_21202(self):
        """
        0x52d2 -> :sswitch_1e
        :return:
        """
        self.result[self.field_map.get('cV', 'cV')] = self.archive_d_b()

    def j_flag_2149(self):
        """
        0x865 -> :sswitch_1f
        :return:
        """
        self.result[self.field_map.get('cU', 'cU')] = self.archive_d_g()

    def j_flag_12841(self):
        """
        0x3229 -> :sswitch_20
        :return:
        """
        self.result[self.field_map.get('cT', 'cT')] = self.archive_d_b()

    def j_flag_36137(self):
        """
        0x8d29 -> :sswitch_21
        :return:
        """
        self.result[self.field_map.get('cS', 'cS')] = self.archive_d_n()

    def j_flag_44133(self):
        """
        0xac65 -> :sswitch_22
        :return:
        """
        self.result[self.field_map.get('cR', 'cR')] = self.archive_d_c()

    def j_flag_60674(self):
        """
        0xed02 -> :sswitch_23
        :return:
        """
        self.result[self.field_map.get('cQ', 'cQ')] = self.archive_d_g()

    def j_flag_39049(self):
        """
        0x9889 -> :sswitch_24
        :return:
        """
        self.result[self.field_map.get('cP', 'cP')] = self.archive_d_a_archive_c()

    def j_flag_55484(self):
        """
        0xd8bc -> :sswitch_25
        :return:
        """
        self.result[self.field_map.get('cO', 'cO')] = self.archive_d_g()

    def j_flag_31178(self):
        """
        0x79ca -> :sswitch_26
        :return:
        """
        self.result[self.field_map.get('cN', 'cN')] = self.archive_d_g()

    def j_flag_42148(self):
        """
        0xa4a4 -> :sswitch_27
        :return:
        """
        self.result[self.field_map.get('cM', 'cM')] = self.archive_d_g()

    def j_flag_27213(self):
        """
        0x6a4d -> :sswitch_28
        :return:
        """
        self.result[self.field_map.get('cL', 'cL')] = self.archive_d_b_archive_c()

    def j_flag_36817(self):
        """
        0x8fd1 -> :sswitch_29
        :return:
        """
        self.result[self.field_map.get('cK', 'cK')] = self.archive_d_c()

    def j_flag_9640(self):
        """
        0x25a8 -> :sswitch_2a
        :return:
        """
        self.result[self.field_map.get('cJ', 'cJ')] = self.archive_d_g()

    def j_flag_28061(self):
        """
        0x6d9d -> :sswitch_2b
        :return:
        """
        self.result[self.field_map.get('cI', 'cI')] = self.archive_d_g()

    def j_flag_58763(self):
        """
        0xe58b -> :sswitch_2c
        :return:
        """
        self.result[self.field_map.get('cH', 'cH')] = self.archive_d_b()

    def j_flag_52996(self):
        """
        0xcf04 -> :sswitch_2d
        :return:
        """
        self.result[self.field_map.get('cG', 'cG')] = self.archive_d_b()

    def j_flag_13490(self):
        """
        0x34b2 -> :sswitch_2e
        :return:
        """
        self.result[self.field_map.get('cF', 'cF')] = self.archive_d_c()

    def j_flag_51425(self):
        """
        0xc8e1 -> :sswitch_2f
        :return:
        """
        self.result[self.field_map.get('cE', 'cE')] = self.archive_d_g()

    def j_flag_5638(self):
        """
        0x1606 -> :sswitch_30
        :return:
        """
        self.result[self.field_map.get('cD', 'cD')] = self.archive_d_a_archive_c()

    def j_flag_42652(self):
        """
        0xa69c -> :sswitch_31
        :return:
        """
        self.result[self.field_map.get('cC', 'cC')] = self.archive_d_g()

    def j_flag_26753(self):
        """
        0x6881 -> :sswitch_32
        :return:
        """
        self.result[self.field_map.get('cB', 'cB')] = self.archive_d_e()

    def j_flag_26758(self):
        """
        0x6886 -> :sswitch_33
        :return:
        """
        self.result[self.field_map.get('cA', 'cA')] = self.archive_d_e()

    def j_flag_4197(self):
        """
        0x1065 -> :sswitch_34
        :return:
        """
        self.result[self.field_map.get('cz', 'cz')] = self.archive_d_c()

    def j_flag_13919(self):
        """
        0x365f -> :sswitch_35
        :return:
        """
        self.result[self.field_map.get('cy', 'cy')] = self.archive_d_g()

    def j_flag_62502(self):
        """
        0xf426 -> :sswitch_36
        :return:
        """
        self.result[self.field_map.get('cx', 'cx')] = self.archive_d_g()

    def j_flag_7060(self):
        """
        0x1b94 -> :sswitch_37
        :return:
        """
        self.result[self.field_map.get('cw', 'cw')] = self.archive_d_c()

    def j_flag_2030(self):
        """
        0x7ee -> :sswitch_38
        :return:
        """
        self.result[self.field_map.get('cv', 'cv')] = self.archive_d_c()

    def j_flag_17885(self):
        """
        0x45dd -> :sswitch_39
        :return:
        """
        self.result[self.field_map.get('cu', 'cu')] = self.archive_d_b()

    def j_flag_10272(self):
        """
        0x2820 -> :sswitch_3a
        :return:
        """
        self.result[self.field_map.get('ct', 'ct')] = self.archive_d_c()

    def j_flag_29207(self):
        """
        0x7217 -> :sswitch_3b
        :return:
        """
        self.result[self.field_map.get('cs', 'cs')] = self.archive_d_b()

    def j_flag_53705(self):
        """
        0xd1c9 -> :sswitch_3c
        :return:
        """
        self.result[self.field_map.get('cr', 'cr')] = self.archive_d_g()

    def j_flag_34575(self):
        """
        0x870f -> :sswitch_3d
        :return:
        """
        self.result[self.field_map.get('cq', 'cq')] = self.archive_d_c()

    def j_flag_41610(self):
        """
        0xa28a -> :sswitch_3e
        :return:
        """
        self.result[self.field_map.get('cp', 'cp')] = self.archive_d_a_archive_c()

    def j_flag_40627(self):
        """
        0x9eb3 -> :sswitch_3f
        :return:
        """
        self.result[self.field_map.get('co', 'co')] = self.archive_d_a_archive_c()

    def j_flag_42996(self):
        """
        0xa7f4 -> :sswitch_40
        :return:
        """
        self.result[self.field_map.get('cn', 'cn')] = self.archive_d_b_archive_c()

    def j_flag_48254(self):
        """
        0xbc7e -> :sswitch_41
        :return:
        """
        self.result[self.field_map.get('cm', 'cm')] = self.archive_d_g()

    def j_flag_43183(self):
        """
        0xa8af -> :sswitch_42
        :return:
        """
        self.result[self.field_map.get('cl', 'cl')] = self.archive_d_g()

    def j_flag_35048(self):
        """
        0x88e8 -> :sswitch_43
        :return:
        """
        self.result[self.field_map.get('ck', 'ck')] = self.archive_d_g()

    def j_flag_29780(self):
        """
        0x7454 -> :sswitch_44
        :return:
        """
        self.result[self.field_map.get('cj', 'cj')] = self.archive_d_c()

    def j_flag_29783(self):
        """
        0x7457 -> :sswitch_45
        :return:
        """
        self.result[self.field_map.get('ci', 'ci')] = self.archive_d_c()

    def j_flag_29782(self):
        """
        0x7456 -> :sswitch_46
        :return:
        """
        self.result[self.field_map.get('ch', 'ch')] = self.archive_d_c()

    def j_flag_4936(self):
        """
        0x1348 -> :sswitch_47
        :return:
        """
        self.result[self.field_map.get('cg', 'cg')] = self.archive_d_c()

    def j_flag_4937(self):
        """
        0x1349 -> :sswitch_48
        :return:
        """
        self.result[self.field_map.get('cf', 'cf')] = self.archive_d_c()

    def j_flag_60598(self):
        """
        0xecb6 -> :sswitch_49
        :return:
        """
        self.result[self.field_map.get('ce', 'ce')] = self.archive_d_c()

    def j_flag_38124(self):
        """
        0x94ec -> :sswitch_4a
        :return:
        """
        self.result[self.field_map.get('cd', 'cd')] = self.archive_d_g()

    def j_flag_61231(self):
        """
        0xef2f -> :sswitch_4b
        :return:
        """
        self.result[self.field_map.get('cc', 'cc')] = self.archive_d_g()

    def j_flag_52122(self):
        """
        0xcb9a -> :sswitch_4c
        :return:
        """
        self.result[self.field_map.get('cb', 'cb')] = self.archive_d_b_archive_c()

    def j_flag_56435(self):
        """
        0xdc73 -> :sswitch_4d
        :return:
        """
        self.result[self.field_map.get('ca', 'ca')] = self.archive_d_a_archive_c()

    def j_flag_22421(self):
        """
        0x5795 -> :sswitch_4e
        :return:
        """
        self.result[self.field_map.get('bZ', 'bZ')] = self.archive_d_g()

    def j_flag_32155(self):
        """
        0x7d9b -> :sswitch_4f
        :return:
        """
        self.result[self.field_map.get('bY', 'bY')] = self.archive_d_c()

    def j_flag_29689(self):
        """
        0x73f9 -> :sswitch_50
        :return:
        """
        self.result[self.field_map.get('bX', 'bX')] = self.archive_d_g()

    def j_flag_40608(self):
        """
        0x9ea0 -> :sswitch_51
        :return:
        """
        self.result[self.field_map.get('bW', 'bW')] = self.archive_d_c()

    def j_flag_22061(self):
        """
        0x562d -> :sswitch_52
        :return:
        """
        self.result[self.field_map.get('bV', 'bV')] = self.archive_d_e()

    def j_flag_48778(self):
        """
        0xbe8a -> :sswitch_53
        :return:
        """
        self.result[self.field_map.get('bU', 'bU')] = self.archive_d_e()

    def j_flag_16859(self):
        """
        0x41db -> :sswitch_54
        :return:
        """
        self.result[self.field_map.get('bT', 'bT')] = self.archive_d_g()

    def j_flag_11524(self):
        """
        0x2d04 -> :sswitch_55
        :return:
        """
        self.result[self.field_map.get('bS', 'bS')] = self.archive_d_g()

    def j_flag_1045(self):
        """
        0x415 -> :sswitch_56
        :return:
        """
        self.result[self.field_map.get('bR', 'bR')] = self.archive_d_g()

    def j_flag_42932(self):
        """
        0xa7b4 -> :sswitch_57
        :return:
        """
        self.result[self.field_map.get('bQ', 'bQ')] = self.archive_d_c()

    def j_flag_17739(self):
        """
        0x454b -> :sswitch_58
        :return:
        """
        self.result[self.field_map.get('bP', 'bP')] = self.archive_d_g()

    def j_flag_60188(self):
        """
        0xeb1c -> :sswitch_59
        :return:
        """
        self.result[self.field_map.get('bO', 'bO')] = self.archive_d_c()

    def j_flag_14389(self):
        """
        0x3835 -> :sswitch_5a
        :return:
        """
        self.result[self.field_map.get('bN', 'bN')] = self.archive_d_c()

    def j_flag_48823(self):
        """
        0xbeb7 -> :sswitch_5b
        :return:
        """
        self.result[self.field_map.get('bM', 'bM')] = self.archive_d_c()

    def j_flag_12028(self):
        """
        0x2efc -> :sswitch_5c
        :return:
        """
        self.result[self.field_map.get('bL', 'bL')] = self.archive_d_g()

    def j_flag_34843(self):
        """
        0x881b -> :sswitch_5d
        :return:
        """
        self.result[self.field_map.get('bK', 'bK')] = self.archive_d_g()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_5e
        :return:
        """
        self.result[self.field_map.get('bJ', 'bJ')] = self.archive_d_g()

    def j_flag_2331(self):
        """
        0x91b -> :sswitch_5f
        :return:
        """
        self.result[self.field_map.get('bI', 'bI')] = self.archive_d_c()

    def j_flag_23196(self):
        """
        0x5a9c -> :sswitch_60
        :return:
        """
        self.result[self.field_map.get('bH', 'bH')] = self.archive_d_c()

    def j_flag_51150(self):
        """
        0xc7ce -> :sswitch_61
        :return:
        """
        self.result[self.field_map.get('bG', 'bG')] = self.archive_d_g()

    def j_flag_8635(self):
        """
        0x21bb -> :sswitch_62
        :return:
        """
        self.result[self.field_map.get('bF', 'bF')] = self.archive_d_n()

    def j_flag_12438(self):
        """
        0x3096 -> :sswitch_63
        :return:
        """
        self.result[self.field_map.get('bE', 'bE')] = self.archive_d_b()

    def j_flag_17541(self):
        """
        0x4485 -> :sswitch_64
        :return:
        """
        self.result[self.field_map.get('bD', 'bD')] = self.archive_d_c()

    def j_flag_34886(self):
        """
        0x8846 -> :sswitch_65
        :return:
        """
        self.result[self.field_map.get('bC', 'bC')] = self.archive_d_g()

    def j_flag_22529(self):
        """
        0x5801 -> :sswitch_66
        :return:
        """
        self.result[self.field_map.get('bB', 'bB')] = self.archive_d_g()

    def j_flag_54393(self):
        """
        0xd479 -> :sswitch_67
        :return:
        """
        self.result[self.field_map.get('bA', 'bA')] = self.archive_d_g()

    def j_flag_54183(self):
        """
        0xd3a7 -> :sswitch_68
        :return:
        """
        self.result[self.field_map.get('bz', 'bz')] = self.archive_d_b()

    def j_flag_60034(self):
        """
        0xea82 -> :sswitch_69
        :return:
        """
        self.result[self.field_map.get('by', 'by')] = self.archive_d_g()

    def j_flag_38658(self):
        """
        0x9702 -> :sswitch_6a
        :return:
        """
        self.result[self.field_map.get('bx', 'bx')] = self.archive_d_b()

    def j_flag_16863(self):
        """
        0x41df -> :sswitch_6b
        :return:
        """
        self.result[self.field_map.get('bw', 'bw')] = self.archive_d_b()

    def j_flag_58943(self):
        """
        0xe63f -> :sswitch_6c
        :return:
        """
        self.result[self.field_map.get('bv', 'bv')] = self.archive_d_b()

    def j_flag_24712(self):
        """
        0x6088 -> :sswitch_6d
        :return:
        """
        self.result[self.field_map.get('bu', 'bu')] = self.archive_d_b_archive_c()

    def j_flag_19057(self):
        """
        0x4a71 -> :sswitch_6e
        :return:
        """
        self.result[self.field_map.get('bt', 'bt')] = self.archive_d_g()

    def j_flag_62985(self):
        """
        0xf609 -> :sswitch_6f
        :return:
        """
        self.result[self.field_map.get('bs', 'bs')] = self.archive_d_b_archive_c()

    def j_flag_42909(self):
        """
        0xa79d -> :sswitch_70
        :return:
        """
        self.result[self.field_map.get('br', 'br')] = self.archive_d_b()

    def j_flag_60796(self):
        """
        0xed7c -> :sswitch_71
        :return:
        """
        self.result[self.field_map.get('bq', 'bq')] = self.archive_d_b()

    def j_flag_18928(self):
        """
        0x49f0 -> :sswitch_72
        :return:
        """
        self.result[self.field_map.get('bp', 'bp')] = self.archive_d_g()

    def j_flag_2126(self):
        """
        0x84e -> :sswitch_73
        :return:
        """
        self.result[self.field_map.get('bo', 'bo')] = self.archive_d_a_archive_c()

    def j_flag_13878(self):
        """
        0x3636 -> :sswitch_74
        :return:
        """
        self.result[self.field_map.get('bn', 'bn')] = self.archive_d_b_archive_c()

    def j_flag_27277(self):
        """
        0x6a8d -> :sswitch_75
        :return:
        """
        self.result[self.field_map.get('bm', 'bm')] = self.archive_d_g()

    def j_flag_43200(self):
        """
        0xa8c0 -> :sswitch_76
        :return:
        """
        self.result[self.field_map.get('bl', 'bl')] = self.archive_d_a_archive_c()

    def j_flag_4549(self):
        """
        0x11c5 -> :sswitch_77
        :return:
        """
        self.result[self.field_map.get('bk', 'bk')] = self.archive_d_g()

    def j_flag_61710(self):
        """
        0xf10e -> :sswitch_78
        :return:
        """
        self.result[self.field_map.get('bj', 'bj')] = self.archive_d_a_archive_c()

    def j_flag_29329(self):
        """
        0x7291 -> :sswitch_79
        :return:
        """
        self.result[self.field_map.get('bi', 'bi')] = self.archive_d_g()

    def j_flag_49258(self):
        """
        0xc06a -> :sswitch_7a
        :return:
        """
        self.result[self.field_map.get('bh', 'bh')] = self.archive_d_a_archive_c()

    def j_flag_5349(self):
        """
        0x14e5 -> :sswitch_7b
        :return:
        """
        self.result[self.field_map.get('bg', 'bg')] = self.archive_d_b_archive_c()

    def j_flag_2454(self):
        """
        0x996 -> :sswitch_7c
        :return:
        """
        self.result[self.field_map.get('bf', 'bf')] = self.archive_d_b()

    def j_flag_9567(self):
        """
        0x255f -> :sswitch_7d
        :return:
        """
        self.result[self.field_map.get('be', 'be')] = self.archive_d_g()

    def j_flag_5957(self):
        """
        0x1745 -> :sswitch_7e
        :return:
        """
        self.result[self.field_map.get('bd', 'bd')] = self.archive_d_b_archive_c()

    def j_flag_57711(self):
        """
        0xe16f -> :sswitch_7f
        :return:
        """
        self.result[self.field_map.get('bc', 'bc')] = self.archive_d_b()

    def j_flag_47602(self):
        """
        0xb9f2 -> :sswitch_80
        :return:
        """
        self.result[self.field_map.get('bb', 'bb')] = self.archive_d_b()

    def j_flag_21649(self):
        """
        0x5491 -> :sswitch_81
        :return:
        """
        self.result[self.field_map.get('ba', 'ba')] = self.archive_d_a_archive_c()

    def j_flag_64158(self):
        """
        0xfa9e -> :sswitch_82
        :return:
        """
        self.result[self.field_map.get('aZ', 'aZ')] = self.archive_d_g()

    def j_flag_42450(self):
        """
        0xa5d2 -> :sswitch_83
        :return:
        """
        self.result[self.field_map.get('aY', 'aY')] = self.archive_d_a_archive_c()

    def j_flag_10935(self):
        """
        0x2ab7 -> :sswitch_84
        :return:
        """
        self.result[self.field_map.get('aX', 'aX')] = self.archive_d_b_archive_c()

    def j_flag_17376(self):
        """
        0x43e0 -> :sswitch_85
        :return:
        """
        self.result[self.field_map.get('aW', 'aW')] = self.archive_d_b()

    def j_flag_63240(self):
        """
        0xf708 -> :sswitch_86
        :return:
        """
        self.result[self.field_map.get('aV', 'aV')] = self.archive_d_b()

    def j_flag_18695(self):
        """
        0x4907 -> :sswitch_87
        :return:
        """
        self.result[self.field_map.get('aU', 'aU')] = self.archive_d_b()

    def j_flag_29739(self):
        """
        0x742b -> :sswitch_88
        :return:
        """
        self.result[self.field_map.get('aT', 'aT')] = self.archive_d_g()

    def j_flag_6617(self):
        """
        0x19d9 -> :sswitch_89
        :return:
        """
        self.result[self.field_map.get('aS', 'aS')] = self.archive_d_b_archive_c()

    def j_flag_39862(self):
        """
        0x9bb6 -> :sswitch_8a
        :return:
        """
        self.result[self.field_map.get('aR', 'aR')] = self.archive_d_b_archive_c()

    def j_flag_36030(self):
        """
        0x8cbe -> :sswitch_8b
        :return:
        """
        self.result[self.field_map.get('aQ', 'aQ')] = self.archive_d_c()

    def j_flag_51306(self):
        """
        0xc86a -> :sswitch_8c
        :return:
        """
        self.result[self.field_map.get('aP', 'aP')] = self.archive_d_b_archive_c()

    def j_flag_39365(self):
        """
        0x99c5 -> :sswitch_8d
        :return:
        """
        self.result[self.field_map.get('aO', 'aO')] = self.archive_d_g()

    def j_flag_3101(self):
        """
        0xc1d -> :sswitch_8e
        :return:
        """
        self.result[self.field_map.get('aN', 'aN')] = self.archive_d_a_archive_c()

    def j_flag_8716(self):
        """
        0x220c -> :sswitch_8f
        :return:
        """
        self.result[self.field_map.get('aM', 'aM')] = self.archive_d_b()

    def j_flag_49683(self):
        """
        0xc213 -> :sswitch_90
        :return:
        """
        self.result[self.field_map.get('aL', 'aL')] = self.archive_d_b()

    def j_flag_32436(self):
        """
        0x7eb4 -> :sswitch_91
        :return:
        """
        self.result[self.field_map.get('aK', 'aK')] = self.archive_d_g()

    def j_flag_26052(self):
        """
        0x65c4 -> :sswitch_92
        :return:
        """
        self.result[self.field_map.get('aJ', 'aJ')] = self.archive_d_b()

    def j_flag_46264(self):
        """
        0xb4b8 -> :sswitch_93
        :return:
        """
        self.result[self.field_map.get('aI', 'aI')] = self.archive_d_g()

    def j_flag_25313(self):
        """
        0x62e1 -> :sswitch_94
        :return:
        """
        self.result[self.field_map.get('aH', 'aH')] = self.archive_d_g()

    def j_flag_33971(self):
        """
        0x84b3 -> :sswitch_95
        :return:
        """
        self.result[self.field_map.get('aG', 'aG')] = self.archive_d_g()

    def j_flag_11711(self):
        """
        0x2dbf -> :sswitch_96
        :return:
        """
        self.result[self.field_map.get('aF', 'aF')] = self.archive_d_g()

    def j_flag_23596(self):
        """
        0x5c2c -> :sswitch_97
        :return:
        """
        self.result[self.field_map.get('aE', 'aE')] = self.archive_d_a_archive_c()

    def j_flag_33237(self):
        """
        0x81d5 -> :sswitch_98
        :return:
        """
        self.result[self.field_map.get('aD', 'aD')] = self.archive_d_b()

    def j_flag_19256(self):
        """
        0x4b38 -> :sswitch_99
        :return:
        """
        self.result[self.field_map.get('aC', 'aC')] = self.archive_d_b()

    def j_flag_30174(self):
        """
        0x75de -> :sswitch_9a
        :return:
        """
        self.result[self.field_map.get('aB', 'aB')] = self.archive_d_g()

    def j_flag_36289(self):
        """
        0x8dc1 -> :sswitch_9b
        :return:
        """
        self.result[self.field_map.get('aA', 'aA')] = self.archive_d_b()

    def j_flag_46226(self):
        """
        0xb492 -> :sswitch_9c
        :return:
        """
        self.result[self.field_map.get('az', 'az')] = self.archive_d_b()

    def j_flag_37291(self):
        """
        0x91ab -> :sswitch_9d
        :return:
        """
        self.result[self.field_map.get('ay', 'ay')] = self.archive_d_g()

    def j_flag_557(self):
        """
        0x22d -> :sswitch_9e
        :return:
        """
        self.result[self.field_map.get('ax', 'ax')] = self.archive_d_a_archive_c()

    def j_flag_35278(self):
        """
        0x89ce -> :sswitch_9f
        :return:
        """
        self.result[self.field_map.get('aw', 'aw')] = self.archive_d_g()

    def j_flag_65252(self):
        """
        0xfee4 -> :sswitch_a0
        :return:
        """
        self.result[self.field_map.get('av', 'av')] = self.archive_d_g()

    def j_flag_32770(self):
        """
        0x8002 -> :sswitch_a1
        :return:
        """
        self.result[self.field_map.get('au', 'au')] = self.archive_d_g()

    def j_flag_11823(self):
        """
        0x2e2f -> :sswitch_a2
        :return:
        """
        self.result[self.field_map.get('at', 'at')] = self.archive_d_g()

    def j_flag_36201(self):
        """
        0x8d69 -> :sswitch_a3
        :return:
        """
        self.result[self.field_map.get('as', 'as')] = self.archive_d_b()

    def j_flag_63354(self):
        """
        0xf77a -> :sswitch_a4
        :return:
        """
        self.result[self.field_map.get('ar', 'ar')] = self.archive_d_a_archive_c()

    def j_flag_59360(self):
        """
        0xe7e0 -> :sswitch_a5
        :return:
        """
        self.result[self.field_map.get('aq', 'aq')] = self.archive_d_g()

    def j_flag_47913(self):
        """
        0xbb29 -> :sswitch_a6
        :return:
        """
        self.result[self.field_map.get('ap', 'ap')] = self.archive_d_b_archive_c()

    def j_flag_20889(self):
        """
        0x5199 -> :sswitch_a7
        :return:
        """
        self.result[self.field_map.get('ao', 'ao')] = self.archive_d_b_archive_c()

    def j_flag_36884(self):
        """
        0x9014 -> :sswitch_a8
        :return:
        """
        self.result[self.field_map.get('an', 'an')] = self.archive_d_a_archive_c()

    def j_flag_20580(self):
        """
        0x5064 -> :sswitch_a9
        :return:
        """
        self.result[self.field_map.get('am', 'am')] = self.archive_d_b()

    def j_flag_13714(self):
        """
        0x3592 -> :sswitch_aa
        :return:
        """
        self.result[self.field_map.get('al', 'al')] = self.archive_d_g()

    def j_flag_54531(self):
        """
        0xd503 -> :sswitch_ab
        :return:
        """
        self.result[self.field_map.get('ak', 'ak')] = self.archive_d_b()

    def j_flag_9253(self):
        """
        0x2425 -> :sswitch_ac
        :return:
        """
        self.result[self.field_map.get('aj', 'aj')] = self.archive_d_b()

    def j_flag_8780(self):
        """
        0x224c -> :sswitch_ad
        :return:
        """
        self.result[self.field_map.get('ai', 'ai')] = self.archive_d_g()

    def j_flag_61577(self):
        """
        0xf089 -> :sswitch_ae
        :return:
        """
        self.result[self.field_map.get('ah', 'ah')] = self.archive_d_a_archive_c()

    def j_flag_48980(self):
        """
        0xbf54 -> :sswitch_af
        :return:
        """
        self.result[self.field_map.get('ag', 'ag')] = self.archive_d_b()

    def j_flag_40067(self):
        """
        0x9c83 -> :sswitch_b0
        :return:
        """
        self.result[self.field_map.get('af', 'af')] = self.archive_d_g()

    def j_flag_42203(self):
        """
        0xa4db -> :sswitch_b1
        :return:
        """
        self.result[self.field_map.get('ae', 'ae')] = self.archive_d_b_archive_c()

    def j_flag_15498(self):
        """
        0x3c8a -> :sswitch_b2
        :return:
        """
        self.result[self.field_map.get('ad', 'ad')] = self.archive_d_c()

    def j_flag_8459(self):
        """
        0x210b -> :sswitch_b3
        :return:
        """
        self.result[self.field_map.get('ac', 'ac')] = self.archive_d_g()

    def j_flag_20970(self):
        """
        0x51ea -> :sswitch_b4
        :return:
        """
        self.result[self.field_map.get('ab', 'ab')] = self.archive_d_b_archive_c()

    def j_flag_24783(self):
        """
        0x60cf -> :sswitch_b5
        :return:
        """
        self.result[self.field_map.get('aa', 'aa')] = self.archive_d_b_archive_c()

    def j_flag_52758(self):
        """
        0xce16 -> :sswitch_b6
        :return:
        """
        self.result[self.field_map.get('Z', 'Z')] = self.archive_d_a_archive_c()

    def j_flag_64842(self):
        """
        0xfd4a -> :sswitch_b7
        :return:
        """
        self.result[self.field_map.get('Y', 'Y')] = self.archive_d_g()

    def j_flag_13928(self):
        """
        0x3668 -> :sswitch_b8
        :return:
        """
        self.result[self.field_map.get('X', 'X')] = self.archive_d_n()

    def j_flag_27635(self):
        """
        0x6bf3 -> :sswitch_b9
        :return:
        """
        self.result[self.field_map.get('W', 'W')] = self.archive_d_n()

    def j_flag_11687(self):
        """
        0x2da7 -> :sswitch_ba
        :return:
        """
        self.result[self.field_map.get('V', 'V')] = self.archive_d_g()

    def j_flag_4409(self):
        """
        0x1139 -> :sswitch_bb
        :return:
        """
        self.result[self.field_map.get('U', 'U')] = self.archive_d_a_archive_c()

    def j_flag_7649(self):
        """
        0x1de1 -> :sswitch_bc
        :return:
        """
        self.result[self.field_map.get('T', 'T')] = self.archive_d_g()

    def j_flag_30359(self):
        """
        0x7697 -> :sswitch_bd
        :return:
        """
        self.result[self.field_map.get('S', 'S')] = self.archive_d_b()

    def j_flag_14531(self):
        """
        0x38c3 -> :sswitch_be
        :return:
        """
        self.result[self.field_map.get('R', 'R')] = self.archive_d_b_archive_c()

    def j_flag_61205(self):
        """
        0xef15 -> :sswitch_bf
        :return:
        """
        self.result[self.field_map.get('Q', 'Q')] = self.archive_d_e()

    def j_flag_13689(self):
        """
        0x3579 -> :sswitch_c0
        :return:
        """
        self.result[self.field_map.get('P', 'P')] = self.archive_d_g()

    def j_flag_15238(self):
        """
        0x3b86 -> :sswitch_c1
        :return:
        """
        self.result[self.field_map.get('O', 'O')] = self.archive_d_g()

    def j_flag_39739(self):
        """
        0x9b3b -> :sswitch_c2
        :return:
        """
        self.result[self.field_map.get('N', 'N')] = self.archive_d_a_archive_c()

    def j_flag_27043(self):
        """
        0x69a3 -> :sswitch_c3
        :return:
        """
        self.result[self.field_map.get('M', 'M')] = self.archive_d_a_archive_c()

    def j_flag_27339(self):
        """
        0x6acb -> :sswitch_c4
        :return:
        """
        self.result[self.field_map.get('L', 'L')] = self.archive_d_g()

    def j_flag_10814(self):
        """
        0x2a3e -> :sswitch_c5
        :return:
        """
        self.result[self.field_map.get('K', 'K')] = self.archive_d_g()

    def j_flag_65486(self):
        """
        0xffce -> :sswitch_c6
        :return:
        """
        self.result[self.field_map.get('J', 'J')] = self.archive_d_g()

    def j_flag_15820(self):
        """
        0x3dcc -> :sswitch_c7
        :return:
        """
        self.result[self.field_map.get('I', 'I')] = self.archive_d_a_archive_c()

    def j_flag_56682(self):
        """
        0xdd6a -> :sswitch_c8
        :return:
        """
        self.result[self.field_map.get('H', 'H')] = self.archive_d_g()

    def j_flag_28220(self):
        """
        0x6e3c -> :sswitch_c9
        :return:
        """
        self.result[self.field_map.get('G', 'G')] = self.archive_d_b_archive_c()

    def j_flag_52597(self):
        """
        0xcd75 -> :sswitch_ca
        :return:
        """
        self.result[self.field_map.get('F', 'F')] = self.archive_d_b_archive_c()

    def j_flag_38206(self):
        """
        0x953e -> :sswitch_cb
        :return:
        """
        self.result[self.field_map.get('E', 'E')] = self.archive_d_b()

    def j_flag_9688(self):
        """
        0x25d8 -> :sswitch_cc
        :return:
        """
        self.result[self.field_map.get('D', 'D')] = self.archive_d_g()

    def j_flag_16128(self):
        """
        0x3f00 -> :sswitch_cd
        :return:
        """
        self.result[self.field_map.get('C', 'C')] = self.archive_d_g()

    def j_flag_6121(self):
        """
        0x17e9 -> :sswitch_ce
        :return:
        """
        self.result[self.field_map.get('B', 'B')] = self.archive_d_b_archive_c()

    def j_flag_23076(self):
        """
        0x5a24 -> :sswitch_cf
        :return:
        """
        self.result[self.field_map.get('A', 'A')] = self.archive_d_b_archive_c()

    def j_flag_14198(self):
        """
        0x3776 -> :sswitch_d0
        :return:
        """
        self.result[self.field_map.get('z', 'z')] = self.archive_d_b_archive_c()

    def j_flag_59858(self):
        """
        0xe9d2 -> :sswitch_d1
        :return:
        """
        self.result[self.field_map.get('y', 'y')] = self.archive_d_a_archive_c()

    def j_flag_40007(self):
        """
        0x9c47 -> :sswitch_d2
        :return:
        """
        self.result[self.field_map.get('x', 'x')] = self.archive_d_g()

    def j_flag_8822(self):
        """
        0x2276 -> :sswitch_d3
        :return:
        """
        self.result[self.field_map.get('w', 'w')] = self.archive_d_a_archive_c()

    def j_flag_12501(self):
        """
        0x30d5 -> :sswitch_d4
        :return:
        """
        self.result[self.field_map.get('v', 'v')] = self.archive_d_g()

    def j_flag_48905(self):
        """
        0xbf09 -> :sswitch_d5
        :return:
        """
        self.result[self.field_map.get('u', 'u')] = self.archive_d_g()

    def j_flag_52575(self):
        """
        0xcd5f -> :sswitch_d6
        :return:
        """
        self.result[self.field_map.get('t', 't')] = self.archive_d_g()

    def j_flag_28655(self):
        """
        0x6fef -> :sswitch_d7
        :return:
        """
        self.result[self.field_map.get('s', 's')] = self.archive_d_a_archive_c()

    def j_flag_3214(self):
        """
        0xc8e -> :sswitch_d8
        :return:
        """
        self.result[self.field_map.get('r', 'r')] = self.archive_d_n()

    def j_flag_50846(self):
        """
        0xc69e -> :sswitch_d9
        :return:
        """
        self.result[self.field_map.get('q', 'q')] = self.archive_d_g()

    def j_flag_25844(self):
        """
        0x64f4 -> :sswitch_da
        :return:
        """
        self.result[self.field_map.get('p', 'p')] = self.archive_d_d()

    def j_flag_44376(self):
        """
        0xad58 -> :sswitch_db
        :return:
        """
        self.result[self.field_map.get('o', 'o')] = self.archive_d_a_archive_c()

    def j_flag_5646(self):
        """
        0x160e -> :sswitch_dc
        :return:
        """
        self.result[self.field_map.get('n', 'n')] = self.archive_d_b_archive_c()

    def j_flag_61595(self):
        """
        0xf09b -> :sswitch_dd
        :return:
        """
        self.result[self.field_map.get('m', 'm')] = self.archive_d_b_archive_c()

    def j_flag_25726(self):
        """
        0x647e -> :sswitch_de
        :return:
        """
        self.result[self.field_map.get('l', 'l')] = self.archive_d_c()

    def j_flag_39023(self):
        """
        0x986f -> :sswitch_df
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_b_archive_c()

    def j_flag_49936(self):
        """
        0xc310 -> :sswitch_e0
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_b_archive_c()

    def j_flag_11393(self):
        """
        0x2c81 -> :sswitch_e1
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_14960(self):
        """
        0x3a70 -> :sswitch_e2
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_b_archive_c()

    def j_flag_63884(self):
        """
        0xf98c -> :sswitch_e3
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_g()

    def j_flag_12917(self):
        """
        0x3275 -> :sswitch_e4
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_b_archive_c()

    def j_flag_60208(self):
        """
        0xeb30 -> :sswitch_e5
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_b_archive_c()

    def j_flag_19540(self):
        """
        0x4c54 -> :sswitch_e6
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_a_archive_c()

    def j_flag_48(self):
        """
        0x30 -> :sswitch_e7
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_a_archive_c()

    def j_flag_18229(self):
        """
        0x4735 -> :sswitch_e8
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
