#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from basefactory import WebdriverOperator
from webWork.pageObject.add_member_page import AddMemberPage


class MainPage(WebdriverOperator):
    def __init__(self):
        super(MainPage, self).__init__()
        locator = 'https://work.weixin.qq.com/wework_admin/frame'
        debugger_address = '127.0.0.1:9222'
        _idOK, self.driver = self.open_url(locator=locator, debugger_address=debugger_address)

    def click_add_member(self):
        """
        点击添加联系人按钮
        :return:
        """
        self.element_click(type='css', locator='.index_service_cnt_itemWrap:nth-child(1)')
        return AddMemberPage(self.driver)
