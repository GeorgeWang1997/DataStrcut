# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: happyNumber.py
@time: 2019-04-11 13:32
"""


def isHappy(n):
    temp = []
    while True:
        n = get_add(n)
        if n == 1:
            return True
        elif n in temp:
            print(temp)
            return False
        else:
            temp.append(n)


def get_add(n):
    res = 0
    while n > 0:
        res += (n % 10) ** 2
        n = int(n / 10)
    return res


print(isHappy(19))