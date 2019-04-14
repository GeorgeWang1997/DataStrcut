# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: binarySearch.py
@time: 2019-04-13 13:31
"""


def binary_search(lst, low, high, value):
    if len(lst) == 0:
        return False
    if low <= high:
        mid = int((low+high)/2)
        if lst[mid] > value:
            return binary_search(lst, low, mid, value)
        elif lst[mid] < value:
            return binary_search(lst, mid, high, value)
        else:
            return mid


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    print(binary_search(lst, 0, 9, 5))

