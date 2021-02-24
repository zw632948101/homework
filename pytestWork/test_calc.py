#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

import allure
import pytest
import yaml


def get_datas(filename):
    """
    读取yaml文件，返回测试数据
    :param filename:
    :return:
    """
    with open(filename, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


@pytest.fixture(autouse=True)
def fixture_test():
    print("开始计算")
    yield
    print("结束计算")


@allure.feature('测试计算器')
class TestCalc:
    @allure.story('测试加法')
    @pytest.mark.add
    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas('../calc/datas/calc_add.yaml'))
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_add(self, get_calc, a, b, expect):
        """
        测试加法
        :param a: 加数
        :param b: 加数
        :param expect: 等于
        :return:
        """
        with allure.step('计算两个数的相加和'):
            result = get_calc.calc_add(a, b)
        pytest.assume(result == expect)

    @allure.story('测试减法')
    @pytest.mark.sub
    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas('../calc/datas/calc_sub.yaml'))
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_sub(self, get_calc, a, b, expect):
        """
        测试加法
        :param a: 被减数
        :param b: 减数
        :param expect: 等于
        :return:
        """
        with allure.step('计算两个数相减'):
            result = get_calc.calc_sub(a, b)
        pytest.assume(result == expect)

    @allure.story('测试乘法')
    @pytest.mark.mul
    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas('../calc/datas/calc_mul.yaml'))
    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_mul(self, get_calc, a, b, expect):
        """
        测试加法
        :param a: 被乘数
        :param b: 乘数
        :param expect: 等于
        :return:
        """
        with allure.step('计算两个数相乘'):
            result = get_calc.calc_mul(a, b)
        pytest.assume(result == expect)

    @allure.story('测试除法法')
    @pytest.mark.div
    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas('../calc/datas/calc_div.yaml'))
    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_div(self, get_calc, a, b, expect):
        """
        测试加法
        :param a: 被除数
        :param b: 除数
        :param expect: 等于
        :return:
        """
        with allure.step('计算两个数相除'):
            result = get_calc.calc_div(a, b)
        pytest.assume(result == expect)
