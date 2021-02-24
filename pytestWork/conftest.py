#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

import pytest

from calc.demo.calc import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc
