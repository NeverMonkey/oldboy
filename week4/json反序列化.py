#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie
import json
import pickle


def sayhi(name):
    print("hello2,", name)


info = {
    'name': 'taihou',
    'age': '18',
    'func': sayhi
}
f = open("info.txt", "rb")

data=pickle.load(f)
# data=pickle.loads(f.read())
print(data["func"]("taihou"))
