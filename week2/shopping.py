#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:taihou.nie
product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120),
]
shopping_list = []
salary = input("\033[34;1mInput your salary:\033[0m")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, goods in enumerate(product_list):
            print(index, goods)
        your_choice = input("\033[32;1m选择你需要的商品编号：\033[0m")
        if your_choice.isdigit():
            your_choice = int(your_choice)
            if your_choice >= 0 and your_choice <= len(product_list):
                your_goods = product_list[your_choice]
                if salary >= your_goods[1]:
                    shopping_list.append(your_goods)
                    salary -= your_goods[1]
                    print("已将{}加入购物车，余额：{}".format(your_goods, salary))
                else:
                    print("余额不足，当前余额：\033[31;1m{}\033[0m".format(salary))
            else:
                print("你选购的商品不在列表中")
        elif your_choice == 'q':
            print("已购买的商品如下：")
            for i in shopping_list:
                print(i)
            print("你的余额为：{}".format(salary))
            exit()
        else:
            print("未有该选项")
