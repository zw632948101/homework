#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/25 11:29
# @Author : wei.zhang
# @File : browseroperator.py
# @Software: PyCharm
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from Util.conf import config
from Util.log import log


class BrowserOperator(object):
    def __init__(self, driver: WebDriver = None):
        BASEFACTORYDIR = os.path.join(os.path.dirname(__file__), "../../driverApp/chromedriver.exe")
        self.driver_path = os.path.abspath(BASEFACTORYDIR)
        self.driver = driver

    def open_url(self, **kwargs):
        """
        打开网页
        :param kwargs:
        :return:
        """
        try:
            url = kwargs['locator']
        except KeyError:
            log.error('没有URL参数')
            return False, '没有URL参数'

        try:
            type = config.get('BROWSER')  # 从配置文件里取浏览器的类型
            if type == 'chrome':
                log.info('使用chrome浏览器进行测试')
                chrome_options = Options()
                # 添加本地调试
                log.info(f'本地调试：{kwargs.get("debugger_address")},为空时不复用浏览器')
                chrome_options.debugger_address = kwargs.get('debugger_address')
                # 禁用Chrome 策略
                # log.info('不打开浏览器视窗')
                # chrome_options.add_argument('disable-infobars')
                # 禁用Chrome弹窗
                # log.info('禁用Chrome开发者弹窗')
                # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
                # 启用Chrome浏览器
                log.info('启用Chrome浏览器')
                self.driver = webdriver.Chrome(options=chrome_options, executable_path=self.driver_path)
                # 将浏览器窗口放大全屏
                log.info('将浏览器窗口放大全屏')
                self.driver.maximize_window()
                # 打开测试地址
                log.info('打开测试地址')
                self.driver.get(url)
            elif type == 'IE':
                log.info('IE 浏览器')
            else:
                log.info('火狐浏览器')
        except Exception as e:
            log.error(e)
            return False, e
        return True, self.driver

    def close_browser(self, **kwargs):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()
        log.info('关闭浏览器成功')
        return True, '关闭浏览器成功'
