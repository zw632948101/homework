#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/19 14:39
# @Author: wei.zhang
# @File : test_demo.py
# @Software: PyCharm
from appiumWork.pageObj.main_page import MainPage


class TestDemo:
    def setup(self):
        self.mainPage = MainPage()

    def test_demo(self):
        self.mainPage.search_send('阿里巴巴')
