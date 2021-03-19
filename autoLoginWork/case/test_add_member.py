#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

import pytest
import yaml

from autoLoginWork.pageObject.main_page import MainPage


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

    def teardown(self):
        self.mainPage.driver.quit()

    @pytest.mark.parametrize(
        ('username', 'english_name', 'acctid', 'phone', 'telephone', 'email', 'adders', 'position'),
        get_datas('../testData/addmember_data.yaml'))
    def test_add_member(self, username, english_name, acctid, phone, telephone, email, adders,
                        position):
        """
        测试添加员工
        :param username:
        :param english_name:
        :param acctid:
        :param phone:
        :param telephone:
        :param email:
        :param adders:
        :param position:
        :return:
        """
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

    def test_import_member(self):
        """
        测试导入员工
        :return:
        """
        mpage = self.mainPage.click_import_member()
        mpage.upload_file_input(
            filepath='/Users/guoyong/Work/0_Product/homework/autoLoginWork/testData/通讯录批量导入模板.xlsx')
        _isOK, filename = mpage.upload_file_name()
        assert '通讯录批量导入模板.xlsx' == filename[0]
        mpage.click_confirm_import_button()

    def test_get_cookies(self):
        cookies = self.mainPage.driver.get_cookies()
        print(cookies)
