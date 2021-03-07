#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'
import pytest

@pytest.mark.parametrize('name',['哈利','何明'])
def test_mm(name):
    print(name)


def test_login():
    print('login')

def test_login_fail():
    print('login')
    assert False
