#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'
from calc.demo import Calculator
import pytest
import yaml


class TestCalc:
    calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open('datas/calc_add.yaml', encoding='utf-8')))
    def test_add(self, a, b, c):
        """
        测试加法
        :param a: 加数
        :param b: 加数
        :param c: 等于
        :return:
        """
        result = self.calc.calc_add(a, b)
        assert result == c

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open('datas/calc_sub.yaml', encoding='utf-8')))
    def test_sub(self, a, b, c):
        """
        测试加法
        :param a: 被减数
        :param b: 减数
        :param c: 等于
        :return:
        """
        result = self.calc.calc_sub(a, b)
        assert result == c

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open('datas/calc_mul.yaml', encoding='utf-8')))
    def test_mul(self, a, b, c):
        """
        测试加法
        :param a: 被乘数
        :param b: 乘数
        :param c: 等于
        :return:
        """
        result = self.calc.calc_mul(a, b)
        assert result == c

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open('datas/calc_div.yaml', encoding='utf-8')))
    def test_mul(self, a, b, c):
        """
        测试加法
        :param a: 被除数
        :param b: 除数
        :param c: 等于
        :return:
        """
        result = self.calc.calc_div(a, b)
        assert result == c