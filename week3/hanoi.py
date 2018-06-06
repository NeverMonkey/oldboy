#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _Author_ = taihou.nie

s = 0


def hanoi(n, a, b, c):
    global s
    if n == 1:
        s += 1
        print("This is the {} step".format(s))
        print(a, '--->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


hanoi(100, 'A', 'B', 'C')
