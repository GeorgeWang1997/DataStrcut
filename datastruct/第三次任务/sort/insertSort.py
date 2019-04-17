# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: insertSort.py
@time: 2019-04-13 14:12
"""


def insert_sort(lst):
    if len(lst) < 2:
        return
    # 默认0位置上元素为有序区，从1位置开始遍历，插入有序区中
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            # 如果小于有序区最后一个元素，则进行交换，进行下一轮比较，如果大于等于最后一个元素，该元素不用交换也达到有序，直接break，开始插入下一个元素
            if lst[j] < lst[j - 1]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            else:
                break


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    insert_sort(lst)
    print(lst)
