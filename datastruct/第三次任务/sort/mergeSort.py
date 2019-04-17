# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: mergeSort.py
@time: 2019-04-13 14:34
"""


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = int(len(lst)/2)
    return merge(merge_sort(lst[0:mid]), merge_sort(lst[mid:]))


def merge(left, right):
    temp = []
    while left and right:
        if left[0] < right[0]:
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
    if len(left) > 0:
        temp.extend(left)
    if len(right) > 0:
        temp.extend(right)
    return temp


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    print(merge_sort(lst))
