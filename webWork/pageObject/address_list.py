#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from webWork.basefactory.webdriveroperator import WebdriverOperator


class AddressList(WebdriverOperator):
    def __init__(self, webdriver=None):
        super(AddressList, self).__init__(driver=webdriver)

    def get_member(self):
        self.web_element_wait(type='css', locator='.member_colRight_memberTable_td:nth-child(2)')
        _isOK, elem_list = self.find_elements(type='css', locator='.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for elem in elem_list:
            names.append(elem.get_attribute('title'))
        return names
