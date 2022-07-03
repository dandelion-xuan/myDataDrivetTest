#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 18:52
# @Author  : xuan
# @Desc    : 
# @File    : test_ids.py
# @Software: PyCharm
import pytest


@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    print(a)


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    print(b)