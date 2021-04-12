#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/19 17:12
# @Author: wei.zhang
# @File : main_page.py
# @Software: PyCharm
from basefactory.APPOperator import AppOperator
from basefactory.webdriveroperator import WebdriverOperator


# from appium.webdriver.webdriver import WebDriver


class MainPage(WebdriverOperator):
    def __init__(self, driver=None):
        super(MainPage, self).__init__()
        self.driver = driver
        if not driver:
            self.driver = AppOperator().open_app()
        self.web_implicitly_wait()

    def click_search(self):
        """
        点击搜索输入框
        :return:
        """
        return self.click(by='id', locator='com.xueqiu.android:id/tv_search')

    def search_send(self, sendNaem):
        """
        输入搜索名称
        :param snedNaem:
        :return:
        """
        return self.element_input(by='id', locator='com.xueqiu.android:id/search_input_text0', input=sendNaem)
