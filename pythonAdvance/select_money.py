#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'
"""
定义工资查询模块 select_money，用来展示工资数额
"""
from money import salary_money


def select_money():
    """
    调用存款变量，并展示
    :return:当前存款
    """
    print(f"当前工资：{salary_money}")
    return salary_money


if __name__ == '__main__':
    select_money()
