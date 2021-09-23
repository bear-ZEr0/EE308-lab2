import unittest
from EE308-lab2 import *


class MyTestCase(unittest.TestCase):


    def test_first(self):
        with open('test.txt') as C_file:
            lines = C_file.readlines()
        lists, total_num = first(lines)
        self.assertEqual(total_num, 35)

    def test_second(self):
        with open('test.txt') as C_file:
            lines = C_file.readlines()
        lists, total_num = first(lines)
        case_nums, switch_nums = second(lists[:])
        self.assertEqual(case_nums, [3, 2])

    def test_third(self):
        with open('test.txt') as C_file:
            lines = C_file.readlines()
        lists, total_num = first(lines)
        if_else_nums, if_elif_nums = third(lists[:])
        self.assertEqual(if_else_nums, 2)

if __name__ == '__main__':
    unittest.main()
