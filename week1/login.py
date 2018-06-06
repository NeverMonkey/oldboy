#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:taihou.nie

# account will be locked when failed three times

import os
import json

user1 = {'name': 'Apple', 'islocked': False, 'password': 'apple'}
user2 = {'name': 'Banana', 'islocked': False, 'password': 'banana'}
user3 = {'name': 'Cherry', 'islocked': False, 'password': 'cherry'}
user_list = [user1, user2, user3]

pwd = os.getcwd()
# pwd=os.path.abspath('.')
filename = 'account.txt'
filepath = os.path.join(pwd, filename)

# 写入初始记录
# with open(filepath, 'w') as file:
#     for i in user_list:
#         json_i = json.dumps(i)
#         file.write(json_i + '\n')

# 读取记录
account_list = []
with open(filepath, 'r') as file:
    new_list = file.read().split('\n')[:-1]
    for x in new_list:
        json_x = json.loads(x)
        account_list.append(json_x)

names = [account_list[i]['name'] for i in range(len(account_list))]

input_name = input("Welcome! \nWhat is your name:")
if input_name in names:
    print("Hello,{}".format(input_name))
else:
    print("{} is not in user list,Bye!".format(input_name))
    exit(1)
# 获取其余信息
for i in range(len(account_list)):
    if account_list[i]['name'] == input_name:
        user_index = i
        user_status = account_list[i]['islocked']
        user_pwd = account_list[i]['password']
if user_status == True:
    print("User {} is locked".format(input_name))
    exit(1)
count = 0
while count < 3:
    input_pwd = input("Please enter you password:")
    if input_pwd == user_pwd:
        print("Nice to meet you")
        exit(0)
    else:
        print("Wrong password,Try again")
    count += 1
else:
    print("Failed three times,we will lock {}".format(input_name))
    account_list[user_index]['islocked'] = True
    print(account_list)
    with open(filepath, 'w') as file:
        for i in account_list:
            json_i = json.dumps(i)
            file.write(json_i + '\n')
