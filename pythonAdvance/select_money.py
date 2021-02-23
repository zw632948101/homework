#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from money import salary_money


def select_money():
    print(f"当前工资：{salary_money}")
    return salary_money

if __name__ == '__main__':
    select_money()