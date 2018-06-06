#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie


import time
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call the function %s():' % func.__name__)
        fn = func(*args, **kw)
        print('end call the function %s():' % func.__name__)
        return fn

    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 首先执行log(text)，返回的是decorator函数
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数。


def log3(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text, str):
                print('%s %s start' % (text, func.__name__))
                _func = func(*args, **kw)
                print('%s %s end' % (text, func.__name__))
            else:
                print('begin call the function %s():' % func.__name__)
                _func = func(*args, **kw)
                print('end call the function %s():' % func.__name__)
            return _func

        return wrapper

    return decorator


@log3()
def now():
    # print(time.localtime())
    print(time.strftime('%Y-%m-%d %X', time.localtime()))
    # return time.strftime('%Y-%m-%d %X', time.localtime())


now()
