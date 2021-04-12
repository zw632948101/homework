#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/31 11:30 
# @Author : wei.zhang
# @File : webdriveroperator.py
# @Software: PyCharm

import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Util.log import log
from Util.conf import get_config, config


class WebdriverOperator:
    def __init__(self, driver: webdriver = None):
        super(WebdriverOperator, self).__init__()
        self.driver = driver
        self.conf = get_config('/Users/guoyong/Work/0_Product/homework/basefactory/by.yaml')
        self.error_cont = 0

    def get_screenshot_as_file(self):
        """
        截屏保存
        :return:返回路径
        """
        pic_name = str(time.time()).replace('.', '') + '.png'
        screent_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f"../SCREENSHOTDIR/{pic_name}"))
        self.driver.get_screenshot_as_file(screent_path)
        return screent_path

    def gotosleep(self, **kwargs):
        time.sleep(3)
        return True, '等待成功'

    def web_implicitly_wait(self, **kwargs):
        """
        隐式等待
        :return:
        by  存时间
        """
        try:
            s = kwargs['time']
        except KeyError:
            s = 10
        try:
            self.driver.implicitly_wait(s)
        except NoSuchElementException:
            log.error('隐式等待 页面元素未加载完成')
            return False, '隐式等待 页面元素未加载完成'
        log.info('隐式等待 元素加载完成')
        return True, '隐式等待 元素加载完成'

    def web_element_wait(self, **kwargs):
        """
        等待元素可见
        :return:
        """
        try:
            by = kwargs['by']
            locator = kwargs['locator']
        except KeyError:
            log.error('未传需要等待元素的定位参数')
            return False, '未传需要等待元素的定位参数'
        try:
            s = kwargs['time']
        except KeyError:
            s = 30
        try:
            if self.conf.get(by):
                WebDriverWait(self.driver, s, 0.5).until(
                    EC.visibility_of_element_located((self.conf.get(by), locator)))
            else:
                log.error('不能识别元素类型[' + by + ']')
                return False, '不能识别元素类型[' + by + ']'
        except NoSuchElementException:
            log.error('元素[' + locator + ']等待出现超时')
            return False, '元素[' + locator + ']等待出现超时'
        log.info('元素[' + locator + ']等待出现成功')
        return True, '元素[' + locator + ']等待出现成功'

    def find(self, by, locator=None):
        """
        查找元素
        :param by:
        :param locator:
        :return:
        """
        try:
            if isinstance(by, tuple):
                elem = self.driver.find_elements(*by)
            else:
                elem = self.driver.find_element(by, locator)
            self.error_cont = 0
            log.info(f'获取元素{by, locator}成功:{elem}')
            return elem
        except Exception as e:
            self.error_cont += 1
            if self.error_cont >= config.get('ERROR_MAX'):
                screenshot_path = self.get_screenshot_as_file()
                log.error(e)
                log.error(f'获取元素{by, locator}失败,已截图[{screenshot_path}].')
                raise e
            for black in config.get('BLACK_LIST'):
                elem = self.driver.find_elements(*black)
                if len(elem) > 0:
                    elem[0].click()
                    return self.find(by, locator)

    def click(self, **kwargs):
        """
        点击
        :param kwargs:
        :return:
        """
        try:
            by = self.conf.get(kwargs['by'])
            locator = kwargs['locator']
            index = kwargs.get('index')
        except KeyError:
            log.error('缺少传参')
            return False, '缺少传参'
        elem = self.find((by, locator))[index] if index else self.find(by, locator)
        try:
            elem.click()
            self.error_cont = 0
            log.info('元素[' + locator + ']点击成功')
            return True, '元素[' + locator + ']点击成功'
        except Exception as e:
            self.error_cont += 1
            if self.error_cont >= config.get('ERROR_MAX'):
                screenshot_path = self.get_screenshot_as_file()
                log.error(e)
                log.error(f'获取元素{by, locator}失败,已截图[{screenshot_path}].')
                raise e
            for black in config.get('BLACK_LIST'):
                elem = self.driver.find_elements(*black)
                if len(elem) > 0:
                    elem[0].click()
                    return self.click(**kwargs)

    def element_input(self, **kwargs):
        """
        输入
        :param kwargs:
        :return:
        """
        try:
            by = kwargs['by']
            locator = kwargs['locator']
            text = str(kwargs['input'])
            index = kwargs.get('index')
        except KeyError:
            return '缺少传参'
        elem = self.find((by, locator))[index] if index else self.find(by, locator)
        try:
            elem.send_keys(text)
            self.error_cont = 0
            log.info(f'元素[{locator}]输入[{text}]成功')
            return True
        except Exception as e:
            self.error_cont += 1
            if self.error_cont >= config.get('ERROR_MAX'):
                screenshot_path = self.get_screenshot_as_file()
                log.error(e)
                log.error(f'获取元素{by, locator}输入{text}失败,已截图[{screenshot_path}].')
                raise e
            for black in config.get('BLACK_LIST'):
                elem = self.driver.find_elements(*black)
                if len(elem) > 0:
                    elem[0].click()
                    return self.element_input(**kwargs)

    def element_title_index(self, **kwargs):
        """
        获取title属性
        :param kwargs:
        :return:
        """
        try:
            by = kwargs['by']
            locator = kwargs['locator']
            text = str(kwargs['title'])
        except KeyError:
            return False, '缺少传参'
        elem = self.find((by, locator))
        index = []
        for i in range(elem):
            title = elem[i].title
            if text == title:
                index.append(i)
        if index == []:
            log.error('元素[' + locator + ']查找[' + text + ']下标失败.')
            return '元素[' + locator + ']查找[' + text + ']下标失败.'
        return index

    def query_element_text(self, **kwargs):
        """
        获取text属性
        :param kwargs:
        :return:
        """
        try:
            by = kwargs['by']
            locator = kwargs['locator']
        except KeyError:
            return '缺少传参'
        elem = self.find((by, locator))
        index = []
        for i in range(len(elem)):
            title = elem[i].text
            index.append(title)
        if index == []:
            log.error('元素[' + locator + ']查找[]下标失败.')
            return '元素[' + locator + ']查找[]下标失败.'
        return index
