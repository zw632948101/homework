#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
"""
定义发工资模块 send_money，用来增加收入计算
"""
__author__ = 'wei.zhang'

from money import saved_money, salary_money


def send_money():
    """
    调用工资变量和存款变量计算发工资后的存款金额
    :return: 发工资后的存款金额
    """
    print(f"未发工资存款为{saved_money}.")
    money = saved_money + salary_money
    print(f"发完工资后存款为{money}")
    return money
