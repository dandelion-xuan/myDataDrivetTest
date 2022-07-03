#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 18:12
# @Author  : xuan
# @Desc    : 
# @File    : test_yield.py
# @Software: PyCharm
import pytest

"""
基本上按传入的顺序调用，
in user, before yield
I am is tmpFuncuser
in drive, before yield
I am is tmpFuncdrive
PASSED                                         [100%]in test_login func
in test_login func end
in drive, after yield
in user, after yield

如果user失败，drive不会执行；如果drive失败，user最终执行yield后的内容
"""


def tmpFunc(s):
    print("I am is tmpFunc" + s)
    # return 5


@pytest.fixture
def user():
    print("in user, before yield")
    yield tmpFunc("user")
    print("in user, after yield")


@pytest.fixture
def drive():
    print("in drive, before yield")
    yield tmpFunc("drive")
    print("in drive, after yield")


def test_login(user, drive):
    print("in test_login func")
    # u = user
    # d = drive
    # print(u)
    # print(d)
    print("in test_login func end")
