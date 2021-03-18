#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from basefactory.webdriveroperator import WebdriverOperator
from webWork.pageObject.add_member_page import AddMemberPage


class MainPage(WebdriverOperator):
    def __init__(self):
        super(MainPage, self).__init__()
        _idOK, self.driver = self.open_url()

    def click_add_member(self):
        """
        点击添加联系人按钮
        :return:
        """
        self.element_click(type='css', locator='.index_service_cnt_itemWrap:nth-child(1)')
        return AddMemberPage(self.driver)
