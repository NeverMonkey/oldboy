#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie

import json
import pickle


def sayhi(name):
    print("hello,", name)


info = {
    'name': 'taihou',
    'age': '18',
    'func': sayhi
}
f = open("info.txt", "wb")

pickle.dump(info, f)
# f.write(pickle.dumps(info))
f.close()
