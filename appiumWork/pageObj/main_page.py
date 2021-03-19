#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/19 17:12
# @Author: wei.zhang
# @File : main_page.py
# @Software: PyCharm
from basefactory.APPOperator import AppOperator
from basefactory.webdriveroperator import WebdriverOperator


class MainPage(WebdriverOperator):
    def __init__(self, driver=None):
        super(MainPage, self).__init__()
        if not driver:
            self.driver = AppOperator().open_app()
        self.driver = driver
        self.web_implicitly_wait()

    def search_send(self, sendNaem):
        """
        输入搜索名称
        :param snedNaem:
        :return:
        """
        return self.element_input(type='id', locator='com.xueqiu.android:id/home_search',
                                  input=sendNaem)
