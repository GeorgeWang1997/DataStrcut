# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: code_02.py
@time: 2019-04-11 13:31
"""


def merge(list1, list2):
    res = []
    while len(list1) > 0 and len(list2) > 0:
        res.append(list1.pop(0) if list1[0] < list2[0] else list2.pop(0))

    res.extend(list1)
    res.extend(list2)
    return res


if __name__ == '__main__':
    list1 = [1, 4, 8, 9, 21, 42]
    list2 = [3, 9, 15, 16, 19, 36, 39, 84, 91, 127]
    print(merge(list1, list2))
