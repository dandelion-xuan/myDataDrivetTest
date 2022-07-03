#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 18:57
# @Author  : xuan
# @Desc    : 
# @File    : test_factory.py
# @Software: PyCharm
import pytest

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record
# @pytest.fixture
# def make_customer_record():
#
#     created_records = []
#
#     def _make_customer_record(name):
#         record = models.Customer(name=name, orders=[])
#         created_records.append(record)
#         return record
#
#     yield _make_customer_record
#
#     for record in created_records:
#         record.destroy()
# @pytest.fixture()
# def make_customer_record(name):
#     return {"name": name, "orders": []}

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    print(customer_1)
    print(customer_2)
    print(customer_3)