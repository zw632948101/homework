#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/18 16:58
# @Author: wei.zhang
# @File : import_member_page.py
# @Software: PyCharm

from basefactory.webdriveroperator import WebdriverOperator


class ImportMemberPage(WebdriverOperator):
    def __init__(self, webdriver=None):
        super(ImportMemberPage, self).__init__(driver=webdriver)

    def upload_file_input(self, filepath):
        """
        上传通讯录文件
        :param filepath:
        :return:
        """
        return self.elements_input(type='css', locator='#js_upload_file_input', input=filepath)

    def upload_file_name(self):
        """
        获取上传文件名称
        :return:
        """
        return self.query_element_text(type='css', locator='#upload_file_name')

    def click_confirm_import_button(self):
        """
        点击确认导入按钮
        :return:
        """
        return self.elements_click(type='css', locator='#submit_csv')

    def click_import_template(self):
        """
        点击填写通讯录模板后导入链接
        :return:
        """
        return self.elements_click(type='css', locator='.js_template_tip a')

    def click_download_template(self):
        """
        点击下载模板按钮
        :return:
        """
        return self.elements_click(type='css', locator='.ww_fileImporter_header a')