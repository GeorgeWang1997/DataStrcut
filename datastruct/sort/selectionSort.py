# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: selectionSort.py
@time: 2019-04-13 14:25
"""


def selection_sort(lst):
    if len(lst) < 2:
        return
    # 遍历整个数组，找到最小的元素，然后与0位置元素交换，再遍历剩下的元素，寻找第二小的元素放在1位置上，以此类推
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    selection_sort(lst)
    print(lst)