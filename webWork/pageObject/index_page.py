#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

class IndexPage:
    def __init__(self, webdriver=None):
        self.driver = webdriver.WebDriver

    def goto_login(self):
