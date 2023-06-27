import unittest
from functions import load_json, sort_filter_by_date, convert_date, mask_card, format_print


class TestFunctions(unittest.TestCase):
    def test_load_json(self):
        self.assertEqual(load_json("test.json"), "test")

    def test_sort_filter_by_date(self):
        self.assertEqual(sort_filter_by_date(load_json("operations_test.json")), load_json("operations_test2.json"))

    def test_convert_date(self):
        self.assertEqual(convert_date("2019-03-03T03:13:18.622393"), "03.03.2019")

    def test_mask_card(self):
        self.assertEqual(mask_card(load_json("operations_test3.json")),
                         ('Visa Classic', '4040 55** **** 7672', 'Visa Platinum', '7825 45** **** 8021'))
        self.assertEqual(mask_card(load_json("operations_test4.json")), ('Счет', '**7521', 'Счет', '**9323'))
        self.assertEqual(mask_card(load_json("operations_test5.json")), ('Visa Gold', '2684 27** **** 7419'))

    def test_format_print(self):
        self.assertEqual(format_print(load_json("operations_test2.json")), "Success")
