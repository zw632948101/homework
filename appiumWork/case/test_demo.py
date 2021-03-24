#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/19 14:39
# @Author: wei.zhang
# @File : test_demo.py
# @Software: PyCharm
from appiumWork.pageObj.main_page import MainPage
import time


class TestDemo:
    def setup(self):
        self.mainPage = MainPage()

    def test_demo(self):
        self.mainPage.click_search()
        self.mainPage.search_send('阿里巴巴')
        time.sleep(10)
