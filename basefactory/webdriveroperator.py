#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/31 11:30 
# @Author : wei.zhang
# @File : webdriveroperator.py
# @Software: PyCharm

import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from Util.log import log
from basefactory.browseroperator import BrowserOperator


class WebdriverOperator(BrowserOperator):
    def __init__(self, driver=None):
        super(WebdriverOperator, self).__init__(driver=driver)

    def get_screenshot_as_file(self):
        """
        截屏保存
        :return:返回路径
        """
        pic_name = str.split(str(time.time()), '.')[0] + str.split(str(time.time()), '.')[
            1] + '.png'
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
        type  存时间
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
            type = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            log.error('未传需要等待元素的定位参数')
            return False, '未传需要等待元素的定位参数'
        try:
            s = kwargs['time']
        except KeyError:
            s = 30
        try:
            if type == 'id':
                WebDriverWait(self.driver, s, 0.5).until(
                    EC.visibility_of_element_located((By.ID, locator)))
            elif type == 'name':
                WebDriverWait(self.driver, s, 0.5).until(
                    EC.visibility_of_element_located((By.NAME, locator)))
            elif type == 'class':
                WebDriverWait(self.driver, s, 0.5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            elif type == 'xpath':
                WebDriverWait(self.driver, s, 0.5).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
            elif type == 'css':
                WebDriverWait(self.driver, s, 0.5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            else:
                log.error('不能识别元素类型[' + type + ']')
                return False, '不能识别元素类型[' + type + ']'
        except NoSuchElementException:
            log.error('元素[' + locator + ']等待出现超时')
            return False, '元素[' + locator + ']等待出现超时'
        log.info('元素[' + locator + ']等待出现成功')
        return True, '元素[' + locator + ']等待出现成功'

    def find_element(self, type, locator):
        """
        定位元素
        :param type:
        :param itor:
        :return:
        """
        type = str.lower(type)
        try:
            if type == 'id':
                elem = self.driver.find_element(By.ID, locator)
            elif type == 'name':
                elem = self.driver.find_element(By.NAME, locator)
            elif type == 'class':
                elem = self.driver.find_element(By.CLASS_NAME, locator)
            elif type == 'xpath':
                elem = self.driver.find_element(By.XPATH, locator)
            elif type == 'css':
                elem = self.driver.find_element(By.CSS_SELECTOR, locator)
            else:
                log.error('不能识别元素类型:[' + type + ']')
                return False, '不能识别元素类型:[' + type + ']'
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            log.error('获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].')
            return False, '获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        log.info(elem)
        return True, elem

    def find_elements(self, type, locator):
        """
        定位元素
        :param type:
        :param itor:
        :return:
        """
        type = str.lower(type)
        try:
            if type == 'id':
                elem = self.driver.find_elements(By.ID, locator)
            elif type == 'name':
                elem = self.driver.find_elements(By.NAME, locator)
            elif type == 'class':
                elem = self.driver.find_elements(By.CLASS_NAME, locator)
            elif type == 'xpath':
                elem = self.driver.find_elements(By.XPATH, locator)
            elif type == 'css':
                elem = self.driver.find_elements(By.CSS_SELECTOR, locator)
            else:
                log.error('不能识别元素类型:[' + type + ']')
                return False, '不能识别元素类型:[' + type + ']'
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            log.error('获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].')
            return False, '获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        log.info(elem)
        return True, elem

    def find_index_elements(self, type, locator, index):
        """
        定位元素
        :param type:
        :param itor:
        :return:
        """

        type = str.lower(type)
        try:
            _isOK, _strLOG = self.find_elements(type, locator)
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            log.error('获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].')
            return False, '获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        return True, _strLOG[index]

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
            log.error('缺少传参')
            return False, '缺少传参'
        try:
            index = kwargs['index']
            if not index:
                index = 0
        except KeyError:
            index = 0
        _isOK, _strLOG = self.find_index_elements(type, locator, index)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        try:
            elem.click()
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            log.error('元素[' + locator + ']点击失败,已截图[' + screenshot_path + '].')
            return False, '元素[' + locator + ']点击失败,已截图[' + screenshot_path + '].'
        log.info('元素[' + locator + ']点击成功')
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
        _isOK, _strLOG = self.find_index_elements(type, locator, index)
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
            log.error('元素[' + locator + ']输入[' + text + ']失败,已截图[' + screenshot_path + '].')
            return False, '元素[' + locator + ']输入[' + text + ']失败,已截图[' + screenshot_path + '].'
        log.info('元素[' + locator + ']输入[' + text + ']成功')
        return True, '元素[' + locator + ']输入[' + text + ']成功'

    def element_title_index(self, **kwargs):
        """
        获取title属性
        :param kwargs:
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
            text = str(kwargs['title'])
        except KeyError:
            return False, '缺少传参'
        _isOK, _strLOG = self.find_elements(type, locator)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        index = []
        for i in range(elem):
            title = elem[i].title
            if text == title:
                index.append(i)
        if index == []:
            log.error('元素[' + locator + ']查找[' + text + ']下标失败.')
            return False, '元素[' + locator + ']查找[' + text + ']下标失败.'
        return True, index

    def query_element_text(self, **kwargs):
        """
        获取text属性
        :param kwargs:
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            return False, '缺少传参'
        _isOK, _strLOG = self.find_elements(type, locator)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        index = []
        for i in range(len(elem)):
            title = elem[i].text
            index.append(title)
        if index == []:
            log.error('元素[' + locator + ']查找[]下标失败.')
            return False, '元素[' + locator + ']查找[]下标失败.'
        return True, index
