#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from webWork.pageObject.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainPage = MainPage()
        self.mainPage.web_implicitly_wait()

    def test_add_member(self):
        mpage = self.mainPage.click_add_member()
        mpage.input_username(name='张三')
        mpage.input_english_name(english_name='小三')
        mpage.input_acctid(acctid='1000001')
        mpage.select_gender()
        mpage.input_phone(phone='15388126072')
        mpage.input_telephone(telephone='02812345687')
        mpage.input_email(email='632948101@qq.com')
        mpage.input_adders(adders='成都市高新区天府大道')
        mpage.input_position(position='测试工程师')
        mpage.cancel_send_invite()
