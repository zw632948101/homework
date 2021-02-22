#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'


class Calculator:

    def __gain_decimals_amount(self, a, b):
        """
        获得小数位数
        :param a:
        :param b:
        :return:
        """
        value_a = 0
        value_b = 0
        if str(a).find('.'):
            value_a = len(str(a).split('.')[-1])
        if str(b).find('.'):
            value_b = len(str(b).split('.')[-1])
        return value_a, value_b

    def calc_add(self, a, b):
        """
        加法
        :param a: 数字类型
        :param b: 数字类型
        :return: 数字类型
        """
        if a > 999999999:
            return '被加数不能大于999999999'
        if a < -999999999:
            return "被加数不能小于-999999999"
        if b > 999999999:
            return '加数不能大于999999999'
        if b < -999999999:
            return "加数不能小于-999999999"
        value_a, value_b = self.__gain_decimals_amount(a, b)
        amount = value_a if value_a > value_b else value_b
        return round(a + b, amount)

    def calc_sub(self, a, b):
        """
        减法
        :param a: 数字类型
        :param b: 数字类型
        :return: 数字
        """
        if a > 999999999:
            return '被减数不能大于999999999'
        if a < -999999999:
            return "被减数不能小于-999999999"
        if b > 999999999:
            return '减数不能大于999999999'
        if b < -999999999:
            return "减数不能小于-999999999"
        value_a, value_b = self.__gain_decimals_amount(a, b)
        amount = value_a if value_a > value_b else value_b
        return round(a - b, amount)

    def calc_mul(self, a, b):
        """
        乘法
        :param a: 数字
        :param b: 数字
        :return: 数字
        """
        if a > 999999999:
            return '被乘数不能大于999999999'
        if a < -999999999:
            return "被乘数不能小于-999999999"
        if b > 999999999:
            return '乘数不能大于999999999'
        if b < -999999999:
            return "乘数不能小于-999999999"
        value_a, value_b = self.__gain_decimals_amount(a, b)
        amount = value_a + value_b
        return round(a * b, amount)

    def calc_div(self, a, b):
        """
        除法
        :param a: 数字
        :param b: 数字
        :return:
        """
        if a > 999999999:
            return '被除数不能大于999999999'
        if a < -999999999:
            return "被除数不能小于-999999999"
        if b > 999999999:
            return '除数不能大于999999999'
        if b < -999999999:
            return "除数不能小于-999999999"
        if b == 0:
            return '除数不能为0'
        value_a, value_b = self.__gain_decimals_amount(a, b)
        amount = value_a + value_b
        return round(a / b, amount)
