# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/13 23:21
"""

from model import add_model, BaseModel


@add_model(0x76cf)
class MeishiShopApiResult(BaseModel):
    field_map = {
        'A': 'targetType',
        'B': 'recResultCount',
        'C': 'moreHotelsEntrance',
        'D': 'currentCategory',
        'E': 'currentRegion',
        'F': 'floorNavs',
        'G': 'currentFloor',
        'H': 'extSearchResult',
        'I': 'selectedDeal',
        'J': 'selectedListUrl',
        'K': 'extSearchResultType',
        'L': 'searchResultExtraInfo',
        'M': 'searchDirectZoneResult',
        'N': 'operatingLocation',
        'O': 'filterNavi',
        'P': 'guideKeywordResult',
        'Q': 'nearbyHeadlineShops',
        'R': 'searchBannerResult',
        'S': 'searchKTVAdResult',
        'T': 'hideAddShop',
        'U': 'specialCategoryFilterNavi',
        'V': 'navigationTitles',
        'W': 'kTVShopListData',
        'X': 'hotelStarAndPriceList',
        'Y': 'hotelFilterList',
        'Z': 'hotelRecommendList',
        'a': 'isSnapshotShow',
        'aa': 'guideAttributeResult',
        'ab': 'searchOperationResult',
        'ac': 'searchFloatCoupon',
        'ad': 'searchMapResult',
        'ae': 'ishourroom',
        'af': 'scenePosition',
        'ag': 'sceneCount',
        'ah': 'sceneList',
        'ai': 'hotwordGroupList',
        'aj': 'modulesConfig',
        'b': 'subFilterNavs',
        'c': 'optimizeAd',
        'd': 'globalSearchResult',
        'e': 'currentMetro',
        'f': 'hotelTuanInfoList',
        'g': 'currentSelect',
        'h': 'selectNavs',
        'i': 'bannerList',
        'j': 'hasBookingInfoFilter',
        'k': 'hasSearchDate',
        'l': 'currentSort',
        'm': 'currentRange',
        'n': 'currentFilter',
        'o': 'adShops',
        'p': 'metroNavs',
        'q': 'rangeNavs',
        'r': 'sortNavs',
        's': 'filterNavs',
        't': 'regionNavs',
        'u': 'categoryNavs',
        'v': 'keywordInfo',
        'w': 'keywordExtendUrl',
        'x': 'keywordExtendTips',
        'y': 'topMallCount',
        'z': 'targetInfo',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_11655(self):
        """
        0x2d87 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('as', 'as')] = self.archive_d_g()

    def j_flag_42085(self):
        """
        0xa465 -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('ar', 'ar')] = self.archive_d_g()

    def j_flag_22275(self):
        """
        0x5703 -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('aq', 'aq')] = self.archive_d_c()

    def j_flag_3851(self):
        """
        0xf0b -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('ap', 'ap')] = self.archive_d_b()

    def j_flag_43620(self):
        """
        0xaa64 -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('ao', 'ao')] = self.archive_d_c()

    def j_flag_6013(self):
        """
        0x177d -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('an', 'an')] = self.archive_d_c()

    def j_flag_9370(self):
        """
        0x249a -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('al', 'al')] = self.archive_d_b_archive_c()

    def j_flag_25237(self):
        """
        0x6295 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('aj', 'aj')] = self.archive_d_n()

    def j_flag_62191(self):
        """
        0xf2ef -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('ai', 'ai')] = self.archive_d_b_archive_c()

    def j_flag_59816(self):
        """
        0xe9a8 -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('ah', 'ah')] = self.archive_d_b_archive_c()

    def j_flag_27979(self):
        """
        0x6d4b -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('ag', 'ag')] = self.archive_d_c()

    def j_flag_19158(self):
        """
        0x4ad6 -> :sswitch_c
        :return:
        """
        self.result[self.field_map.get('af', 'af')] = self.archive_d_c()

    def j_flag_12585(self):
        """
        0x3129 -> :sswitch_d
        :return:
        """
        self.result[self.field_map.get('ae', 'ae')] = self.archive_d_c()

    def j_flag_47793(self):
        """
        0xbab1 -> :sswitch_e
        :return:
        """
        self.result[self.field_map.get('ad', 'ad')] = self.archive_d_a_archive_c()

    def j_flag_25952(self):
        """
        0x6560 -> :sswitch_f
        :return:
        """
        self.result[self.field_map.get('ac', 'ac')] = self.archive_d_a_archive_c()

    def j_flag_9412(self):
        """
        0x24c4 -> :sswitch_10
        :return:
        """
        self.result[self.field_map.get('ab', 'ab')] = self.archive_d_a_archive_c()

    def j_flag_12722(self):
        """
        0x31b2 -> :sswitch_11
        :return:
        """
        self.result[self.field_map.get('aa', 'aa')] = self.archive_d_a_archive_c()

    def j_flag_10034(self):
        """
        0x2732 -> :sswitch_12
        :return:
        """
        self.result[self.field_map.get('Z', 'Z')] = self.archive_d_a_archive_c()

    def j_flag_1255(self):
        """
        0x4e7 -> :sswitch_13
        :return:
        """
        self.result[self.field_map.get('Y', 'Y')] = self.archive_d_b_archive_c()

    def j_flag_5910(self):
        """
        0x1716 -> :sswitch_14
        :return:
        """
        self.result[self.field_map.get('X', 'X')] = self.archive_d_b_archive_c()

    def j_flag_57935(self):
        """
        0xe24f -> :sswitch_15
        :return:
        """
        self.result[self.field_map.get('W', 'W')] = self.archive_d_a_archive_c()

    def j_flag_37251(self):
        """
        0x9183 -> :sswitch_16
        :return:
        """
        self.result[self.field_map.get('V', 'V')] = self.archive_d_g()

    def j_flag_51735(self):
        """
        0xca17 -> :sswitch_17
        :return:
        """
        self.result[self.field_map.get('U', 'U')] = self.archive_d_a_archive_c()

    def j_flag_62640(self):
        """
        0xf4b0 -> :sswitch_18
        :return:
        """
        self.result[self.field_map.get('T', 'T')] = self.archive_d_b()

    def j_flag_5063(self):
        """
        0x13c7 -> :sswitch_19
        :return:
        """
        self.result[self.field_map.get('S', 'S')] = self.archive_d_a_archive_c()

    def j_flag_11156(self):
        """
        0x2b94 -> :sswitch_1a
        :return:
        """
        self.result[self.field_map.get('R', 'R')] = self.archive_d_a_archive_c()

    def j_flag_29250(self):
        """
        0x7242 -> :sswitch_1b
        :return:
        """
        self.result[self.field_map.get('Q', 'Q')] = self.archive_d_b_archive_c()

    def j_flag_54657(self):
        """
        0xd581 -> :sswitch_1c
        :return:
        """
        self.result[self.field_map.get('P', 'P')] = self.archive_d_a_archive_c()

    def j_flag_355(self):
        """
        0x163 -> :sswitch_1d
        :return:
        """
        self.result[self.field_map.get('O', 'O')] = self.archive_d_a_archive_c()

    def j_flag_55602(self):
        """
        0xd932 -> :sswitch_1e
        :return:
        """
        self.result[self.field_map.get('N', 'N')] = self.archive_d_b_archive_c()

    def j_flag_2106(self):
        """
        0x83a -> :sswitch_1f
        :return:
        """
        self.result[self.field_map.get('M', 'M')] = self.archive_d_a_archive_c()

    def j_flag_37260(self):
        """
        0x918c -> :sswitch_20
        :return:
        """
        self.result[self.field_map.get('L', 'L')] = self.archive_d_g()

    def j_flag_46140(self):
        """
        0xb43c -> :sswitch_21
        :return:
        """
        self.result[self.field_map.get('K', 'K')] = self.archive_d_c()

    def j_flag_5385(self):
        """
        0x1509 -> :sswitch_22
        :return:
        """
        self.result[self.field_map.get('J', 'J')] = self.archive_d_g()

    def j_flag_20727(self):
        """
        0x50f7 -> :sswitch_23
        :return:
        """
        self.result[self.field_map.get('I', 'I')] = self.archive_d_a_archive_c()

    def j_flag_37230(self):
        """
        0x916e -> :sswitch_24
        :return:
        """
        self.result[self.field_map.get('H', 'H')] = self.archive_d_b_archive_c()

    def j_flag_4550(self):
        """
        0x11c6 -> :sswitch_25
        :return:
        """
        self.result[self.field_map.get('G', 'G')] = self.archive_d_a_archive_c()

    def j_flag_23778(self):
        """
        0x5ce2 -> :sswitch_26
        :return:
        """
        self.result[self.field_map.get('F', 'F')] = self.archive_d_b_archive_c()

    def j_flag_62309(self):
        """
        0xf365 -> :sswitch_27
        :return:
        """
        self.result[self.field_map.get('E', 'E')] = self.archive_d_a_archive_c()

    def j_flag_16528(self):
        """
        0x4090 -> :sswitch_28
        :return:
        """
        self.result[self.field_map.get('D', 'D')] = self.archive_d_a_archive_c()

    def j_flag_9052(self):
        """
        0x235c -> :sswitch_29
        :return:
        """
        self.result[self.field_map.get('C', 'C')] = self.archive_d_a_archive_c()

    def j_flag_18986(self):
        """
        0x4a2a -> :sswitch_2a
        :return:
        """
        self.result[self.field_map.get('B', 'B')] = self.archive_d_c()

    def j_flag_45912(self):
        """
        0xb358 -> :sswitch_2b
        :return:
        """
        self.result[self.field_map.get('A', 'A')] = self.archive_d_c()

    def j_flag_26162(self):
        """
        0x6632 -> :sswitch_2c
        :return:
        """
        self.result[self.field_map.get('z', 'z')] = self.archive_d_g()

    def j_flag_40555(self):
        """
        0x9e6b -> :sswitch_2d
        :return:
        """
        self.result[self.field_map.get('y', 'y')] = self.archive_d_c()

    def j_flag_13920(self):
        """
        0x3660 -> :sswitch_2e
        :return:
        """
        self.result[self.field_map.get('x', 'x')] = self.archive_d_g()

    def j_flag_20819(self):
        """
        0x5153 -> :sswitch_2f
        :return:
        """
        self.result[self.field_map.get('w', 'w')] = self.archive_d_g()

    def j_flag_38889(self):
        """
        0x97e9 -> :sswitch_30
        :return:
        """
        self.result[self.field_map.get('v', 'v')] = self.archive_d_g()

    def j_flag_29406(self):
        """
        0x72de -> :sswitch_31
        :return:
        """
        self.result[self.field_map.get('u', 'u')] = self.archive_d_b_archive_c()

    def j_flag_22734(self):
        """
        0x58ce -> :sswitch_32
        :return:
        """
        self.result[self.field_map.get('t', 't')] = self.archive_d_b_archive_c()

    def j_flag_341(self):
        """
        0x155 -> :sswitch_33
        :return:
        """
        self.result[self.field_map.get('s', 's')] = self.archive_d_b_archive_c()

    def j_flag_11371(self):
        """
        0x2c6b -> :sswitch_34
        :return:
        """
        self.result[self.field_map.get('r', 'r')] = self.archive_d_b_archive_c()

    def j_flag_10447(self):
        """
        0x28cf -> :sswitch_35
        :return:
        """
        self.result[self.field_map.get('q', 'q')] = self.archive_d_b_archive_c()

    def j_flag_56769(self):
        """
        0xddc1 -> :sswitch_36
        :return:
        """
        self.result[self.field_map.get('p', 'p')] = self.archive_d_b_archive_c()

    def j_flag_8294(self):
        """
        0x2066 -> :sswitch_37
        :return:
        """
        self.result[self.field_map.get('o', 'o')] = self.archive_d_b_archive_c()

    def j_flag_30905(self):
        """
        0x78b9 -> :sswitch_38
        :return:
        """
        self.result[self.field_map.get('n', 'n')] = self.archive_d_a_archive_c()

    def j_flag_1021(self):
        """
        0x3fd -> :sswitch_39
        :return:
        """
        self.result[self.field_map.get('m', 'm')] = self.archive_d_a_archive_c()

    def j_flag_60840(self):
        """
        0xeda8 -> :sswitch_3a
        :return:
        """
        self.result[self.field_map.get('l', 'l')] = self.archive_d_a_archive_c()

    def j_flag_30151(self):
        """
        0x75c7 -> :sswitch_3b
        :return:
        """
        self.result[self.field_map.get('k', 'k')] = self.archive_d_b()

    def j_flag_576(self):
        """
        0x240 -> :sswitch_3c
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_b()

    def j_flag_13146(self):
        """
        0x335a -> :sswitch_3d
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_b_archive_c()

    def j_flag_14071(self):
        """
        0x36f7 -> :sswitch_3e
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_b_archive_c()

    def j_flag_64458(self):
        """
        0xfbca -> :sswitch_3f
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_a_archive_c()

    def j_flag_43288(self):
        """
        0xa918 -> :sswitch_40
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_b_archive_c()

    def j_flag_54697(self):
        """
        0xd5a9 -> :sswitch_41
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_a_archive_c()

    def j_flag_41585(self):
        """
        0xa271 -> :sswitch_42
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_a_archive_c()

    def j_flag_12561(self):
        """
        0x3111 -> :sswitch_43
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_a_archive_c()

    def j_flag_52094(self):
        """
        0xcb7e -> :sswitch_44
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_a_archive_c()

    def j_flag_3635(self):
        """
        0xe33 -> :sswitch_45
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_b()
