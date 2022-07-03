#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 16:31
# @Author  : xuan
# @Desc    : 
# @File    : emaillib.py
# @Software: PyCharm
class MailAdminClient:
    def create_user(self):
        return MailUser()

    def delete_user(self, user):
        # do some cleanup
        pass


class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, other):
        other.inbox.append(email)

    def clear_mailbox(self):
        self.inbox.clear()


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body