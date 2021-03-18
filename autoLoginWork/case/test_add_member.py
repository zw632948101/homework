#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

import pytest
import yaml

from webWork.pageObject.main_page import MainPage


def get_datas(filename):
    """
    读取yaml文件，返回测试数据
    :param filename:
    :return:
    """
    with open(filename, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


class TestContact:
    def setup(self):
        self.mainPage = MainPage()
        self.mainPage.web_implicitly_wait()

    @pytest.mark.parametrize(
        ('username', 'english_name', 'acctid', 'phone', 'telephone', 'email', 'adders', 'position'),
        get_datas('../testData/addmember_data.yaml'))
    def test_add_member(self, username, english_name, acctid, phone, telephone, email, adders, position):
        mpage = self.mainPage.click_add_member()
        mpage.input_username(name=username)
        mpage.input_english_name(english_name=english_name)
        mpage.input_acctid(acctid=acctid)
        mpage.select_gender()
        mpage.input_phone(phone=phone)
        mpage.input_telephone(telephone=telephone)
        mpage.input_email(email=email)
        mpage.input_adders(adders=adders)
        mpage.input_position(position=position)
        mpage.cancel_send_invite()
        addersspage = mpage.click_save()
        names = addersspage.get_member()
        assert username in names
