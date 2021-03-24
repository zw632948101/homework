#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from basefactory.webdriveroperator import WebdriverOperator
from autoLoginWork.pageObject.address_list_page import AddressListPage


class AddMemberPage(WebdriverOperator):
    def __init__(self, webdriver=None):
        super(AddMemberPage, self).__init__(driver=webdriver)

    def input_username(self, name: str = None):
        """
        输入联系人
        :param name:
        :return:
        """
        if not name:
            return False, '联系人不能为空'
        return self.elements_input(type='css', locator='#username', input=name)

    def input_english_name(self, english_name=None):
        """
        输入别名
        :param english_name:
        :return:
        """
        if not english_name:
            return True, '别名为空'
        return self.elements_input(type='css', locator='#memberAdd_english_name', input=english_name)

    def input_acctid(self, acctid=None):
        """
        输入唯一账号
        :param acctid:
        :return:
        """
        if not acctid:
            return False, '账号不能为空'
        return self.elements_input(type='css', locator='#memberAdd_acctid', input=acctid)

    def select_gender(self, gender=None):
        """
        选择性别
        :param gender:
        :return:
        """
        return self.elements_click(type='css', locator='[name=gender]', index=gender)

    def input_phone(self, phone=None):
        """
        输入手机号
        :param phone:
        :return:
        """
        if not phone:
            return True, '手机号为空'
        return self.elements_input(type='css', locator='#memberAdd_phone', input=phone)

    def input_telephone(self, telephone=None):
        """
        输入座机号
        :param telephone:
        :return:
        """
        if not telephone:
            return True, '座机号为空'
        return self.elements_input(type='css', locator='#memberAdd_telephone', input=telephone)

    def input_email(self, email=None):
        """
        输入邮箱
        :param email:
        :return:
        """
        if not email:
            return True, '邮箱为空'
        return self.elements_input(type='css', locator='#memberAdd_mail', input=email)

    def input_adders(self, adders=None):
        """
        输入地址
        :param adders:
        :return:
        """
        if not adders:
            return True, '地址为空'
        return self.elements_input(type='css', locator='#memberEdit_address', input=adders)

    def click_department_more(self):
        """
        点击部门右侧更多按钮展示删除选项
        :return:
        """
        return self.elements_click(type='css', locator='.js_opt_party')

    def click_remove(self):
        """
        点击部门右侧更多按钮展开额删除选项
        :return:
        """
        return self.elements_click(type='css', locator='.member_party_set_item')

    def click_modification(self):
        """
        点击部门右侧修改按钮
        :return:
        """
        return self.elements_click(type='css', locator='.js_show_party_selector')

    def input_popup_department_search(self, input=None):
        """
        修改部门弹窗搜索框输入搜索关键字
        :param input:
        :return:
        """
        if not input:
            return True, '部门弹窗搜索框输入搜索关键字为空'
        return self.elements_input(type='xpath', locator='//*[@id="memberSearchInput"]', index=1, input=input)

    def find_select_department(self):
        """
        查找已选择的部门
        :return:
        """
        _isOk, index = self.find_elements(type='css', locator='.js_delete')
        return _isOk, index[-1]

    def delete_select_department(self, index=None):
        """
        删除已选的部门
        :param index:
        :return:
        """
        return self.elements_click(type='css', locator='.js_show_party_selector', index=index)

    def select_department_index(self, title: str = None):
        """
        以title精确查找元素下标集
        :param title:
        :return:
        """
        _isOK, indexs = self.element_title_index(type='xpath', locator='//*[@id="searchResult"]/ul/li', title=title)
        if len(indexs) > 1:
            indexs.pop(0)
        return _isOK, indexs[0]

    def select_department(self, index=None):
        """
        选择部门
        :param index:
        :return:
        """
        return self.elements_click(type='xpath', locator='//*[@id="searchResult"]/ul/li', index=index)

    def click_select_department_save(self):
        """
        选择部门后保存
        :return:
        """
        return self.elements_click(type='css', locator='.js_submit', index=-1)

    def click_select_department_cancel(self):
        """
        点击选择成员部门取消按钮
        :return:
        """
        return self.elements_click(type='css', locator='.js_cancel', index=-1)

    def input_position(self, position=None):
        """
        输入职务
        :param input:
        :return:
        """
        if not position:
            return True, '职位为空'
        return self.elements_input(type='css', locator='#memberAdd_title', input=position)

    def select_identity(self, index=None):
        """
        选择身份
        :param index:
        :return:
        """
        return self.elements_click(type='css', locator='[name=identity_stat]', index=index)

    def cancel_send_invite(self):
        """
        点击通过邮件或短信发送企业邀请复选框
        :param index:
        :return:
        """
        return self.elements_click(type='css', locator='[name=sendInvite]')

    def input_extern_position(self, input=None):
        """
        输入对外信息的职务
        :param input:
        :return:
        """
        if not input:
            return True, '对外信息的职务为空'
        return self.elements_input(type='css', locator='[name=extern_position]', input=input)

    def select_position(self, index=None):
        """
        选择对外信息的职务
        :param index:
        :return:
        """
        return self.elements_click(type='css', locator='[name=extern_position_set]', index=index)

    def click_save_and_continue_add(self, index=None):
        """
        index = None 点击上方的保存并继续添加按钮
        index = 1 点击下方的保存并继续添加按钮
        :param index:
        :return:
        """
        return self.elements_click(type='css', locator='.js_btn_continue', index=index)

    def click_cancel(self, index=None):
        """
        index = None 点击上方的取消按钮
        index = 1 点击下方的取消按钮
        :param index:
        :return:
        """
        return self.elements_click(type='css', locator='.js_btn_cancel', index=index)

    def click_save(self, index=None):
        """
        不传index 点击上方的保存按钮
        index传1 点击下方的保存按钮
        :param index:
        :return:
        """
        self.elements_click(type='css', locator='.js_btn_save', index=index)
        return AddressListPage(self.driver)
