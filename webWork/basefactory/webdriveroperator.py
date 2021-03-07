#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/31 11:30 
# @Author : wei.zhang
# @File : webdriveroperator.py
# @Software: PyCharm

import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class WebdriverOperator(object):

    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_screenshot_as_file(self):
        """
        截屏保存
        :return:返回路径
        """
        pic_name = str.split(str(time.time()), '.')[0] + str.split(str(time.time()), '.')[1] + '.png'
        screent_path = os.path.join('SCREENSHOTDIR', pic_name)
        self.driver.get_screenshot_as_file(screent_path)
        return screent_path

    def gotosleep(self, **kwargs):
        time.sleep(3)
        return True, '等待成功'

    def web_implicitly_wait(self, **kwargs):
        """
        隐式等待
        :return:
        type  存时间
        """
        try:
            s = kwargs['time']
        except KeyError:
            s = 10
        try:
            self.driver.implicitly_wait(s)
        except NoSuchElementException:
            return False, '隐式等待 页面元素未加载完成'
        return True, '隐式等待 元素加载完成'

    def web_element_wait(self, **kwargs):
        """
        等待元素可见
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            return False, '未传需要等待元素的定位参数'
        try:
            s = kwargs['time']
        except KeyError:
            s = 30
        try:
            if type == 'id':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.ID, locator)))
            elif type == 'name':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.NAME, locator)))
            elif type == 'class':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            elif type == 'xpath':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            elif type == 'css':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            else:
                return False, '不能识别元素类型[' + type + ']'
        except NoSuchElementException:
            return False, '元素[' + locator + ']等待出现超时'
        return True, '元素[' + locator + ']等待出现成功'

    def find_element(self, type, locator, index=0):
        """
        定位元素
        :param type:
        :param itor:
        :param index:
        :return:
        """
        # isinstance(self.driver, selenium.webdriver.Chrome.)
        type = str.lower(type)
        try:
            if type == 'id':
                elem = self.driver.find_elements_by_id(locator)[index]
            elif type == 'name':
                elem = self.driver.find_elements_by_name(locator)[index]
            elif type == 'class':
                elem = self.driver.find_elements_by_class_name(locator)[index]
            elif type == 'xpath':
                elem = self.driver.find_elements_by_xpath(locator)[index]
            elif type == 'css':
                elem = self.driver.find_elements_by_css_selector(locator)[index]
            else:
                return False, '不能识别元素类型:[' + type + ']'
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        return True, elem

    def element_click(self, **kwargs):
        """
        点击
        :param kwargs:
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']

        except KeyError:
            return False, '缺少传参'
        try:
            index = kwargs['index']
        except KeyError:
            index = 0
        _isOK, _strLOG = self.find_element(type, locator, index)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        try:
            elem.click()
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']点击失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']点击成功'

    def element_input(self, **kwargs):
        """
        输入
        :param kwargs:
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
            text = str(kwargs['input'])
        except KeyError:
            return False, '缺少传参'
        try:
            index = kwargs['index']
        except KeyError:
            index = 0
        _isOK, _strLOG = self.find_element(type, locator, index)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        # if 'test' != elem.get_property('type'):     #校验元素是不是text输入框
        #     screenshot_path = self.get_screenshot_as_file()
        #     return False, '元素['+ itor +']不是输入框,输入失败,已截图[' + screenshot_path + '].'
        try:
            elem.send_keys(text)
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']输入[' + text + ']失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']输入[' + text + ']成功'