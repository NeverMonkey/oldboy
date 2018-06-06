#!/usr/bin/env python
#_*_coding:utf-8_*_
#author:taihou.nie

with open('test.txt','w+b') as f:
    f.write('大王叫我来巡山'.encode('utf-8'))
    print(f.tell())              #查看当前指针所在位置为21

    f.seek(3,0)                  #以文件开头为起始，移动3个字节，移过了中文字符'大'
    print(f.tell())              #查看当前指针所在位置为3

    print(f.read(3).decode('utf-8'))     #再读取3个字节，解码的结果为字符'好'