# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: minHeap.py
@time: 2019-04-18 13:55
"""


def min_heap(lst, index):
    father_index = int((index-1)/2)
    while lst[index] < lst[father_index]:
        lst[index], lst[father_index] = lst[father_index], lst[index]
        index = father_index
        father_index = int((index-1)/2)


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    for i in range(len(lst)):
        min_heap(lst, i)
    print(lst)
