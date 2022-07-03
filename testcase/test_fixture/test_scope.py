#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 17:13
# @Author  : xuan
# @Desc    : 
# @File    : test_scope.py
# @Software: PyCharm
import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")


class TestOne:
    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert order == ["one", "outer"]


class TestTwo:
    @pytest.fixture
    def inner(self, order):
        order.append("two")

    def test_order(self, order, outer):
        assert order == ["two", "outer"]