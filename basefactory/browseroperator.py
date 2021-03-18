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
        self.driver = driver

    def open_url(self, **kwargs):
        """
        打开网页
        :param kwargs:
        :return:
        """
        import platform
        system = platform.system()
        if system == 'Windows':
            find_util = 'chromedriver.exe'
        else:
            find_util = 'chromedriver'
        BASEFACTORYDIR = os.path.join(os.path.dirname(__file__), "./../driverApp/" + find_util)
        driver_path = os.path.abspath(BASEFACTORYDIR)
        log.info(driver_path)
        try:
            url = kwargs['locator']
        except KeyError:
            url = config.get('LOCATOR')
            if not url:
                return False, '没有URL参数'

        try:
            type = config.get('BROWSER')  # 从配置文件里取浏览器的类型
            cookies = config.get('COOKIES')
            debugmode = config.get('DEBUG_MODE')
            if type == 'chrome':
                log.info('使用chrome浏览器进行测试')
                # 添加本地调试
                if debugmode == 'debugger':
                    chrome_options = Options()
                    log.info(f'本地调试：{config.get("DEBUGGER_ADDERESS")},为空时不复用浏览器')
                    chrome_options.debugger_address = config.get('DEBUGGER_ADDERESS')
                else:
                    chrome_options = webdriver.ChromeOptions()
                    # 不打开浏览器视窗
                    if config.get('HEADLESS'):
                        log.info('不打开浏览器视窗')
                        chrome_options.add_argument('headless')
                    # 禁用Chrome弹窗
                    log.info('禁用Chrome开发者弹窗')
                    chrome_options.add_argument('disable-infobars')
                    chrome_options.add_experimental_option("useAutomationExtension", False)
                    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
                # 启用Chrome浏览器
                log.info('启用Chrome浏览器')
                self.driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
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
            if debugmode == 'cookies':
                log.info('使用cookies测试')
                for cookie in cookies:
                    if 'expiry' in cookie.keys():
                        cookie.pop('expiry')
                    self.driver.add_cookie(cookie)
                self.driver.refresh()
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
