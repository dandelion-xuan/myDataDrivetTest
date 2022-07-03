#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 16:32
# @Author  : xuan
# @Desc    : 
# @File    : test_emaillib.py
# @Software: PyCharm
import pytest
from entity.emaillib import Email, MailAdminClient

"""
yield遵循规律：先调用后清除，后调用先清除
场景：A send mail to B ,assert B recevie the mail.Aseert before A clear.
"""
@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


def test_email_received(sending_user, receiving_user):
    email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox