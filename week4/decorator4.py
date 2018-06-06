#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie

user = 'taihou'
passwd = 'neonie'


def auth(func):
    def wrapper(*args, **kw):
        username = input("Username:").strip()
        password = input("Password:").strip()
        if username == user and passwd == password:
            print("Success")
        else:
            print("Failed")

    return wrapper


def index():
    print("Welcome to index page")


@auth
def home():
    print("Welcome to home page")


def bbs():
    print("Welcome to bbs page")


home()
