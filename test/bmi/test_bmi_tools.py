#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : André Böni
# Created Date: 18/10/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" This class tests the calc_bmi function of the bmi_tools module in bmi"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import unittest
from bmi.bmi_tools import calc_bmi, validate_height, validate_weight


class TestCalcBMI(unittest.TestCase):
    def test_good_case(self):
        height = 1.88
        weight = 82
        bmi = calc_bmi(height, weight)
        self.assertEqual(bmi, 23.2, "BMI calculation is wrong")

    def test_wrong_height(self):
        height = 2.6
        weight = 82
        with self.assertRaises(Exception):
            calc_bmi(height, weight)

    def test_wrong_weight(self):
        height = 1.88
        weight = 161
        with self.assertRaises(Exception):
            calc_bmi(height, weight)

    def test_wrong_weight_and_weight(self):
        height = 2.6
        weight = 161
        with self.assertRaises(Exception):
            calc_bmi(height, weight)


class TestValidateHeight(unittest.TestCase):
    def test_good_case(self):
        height = 1.88
        self.assertEqual(validate_height(height), True)

    def test_bad_case(self):
        height = 2.6
        self.assertEqual(validate_height(height), False)


class TestValidateWeight(unittest.TestCase):
    def test_good_case(self):
        weight = 86
        self.assertEqual(validate_weight(weight), True)

    def test_bad_case(self):
        weight = 161
        self.assertEqual(validate_weight(weight), False)


if __name__ == '__main__':
    unittest.main()
