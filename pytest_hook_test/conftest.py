#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

import pytest


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)
    items.reverse()


def pytest_addoption(parser):
    mygroup = parser.getgroup('hogwarts')
    mygroup.addoption("--env", default='test', test='env', help='set your run env')


def cmdoption(request):
    env = request.config.getoption('--env', default='test')
    if env == 'test':
        print(env)
    if env == 'dev':
        print(env)
