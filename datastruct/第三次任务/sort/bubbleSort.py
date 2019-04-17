# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: bubbleSort.py
@time: 2019-04-13 13:42
"""


def bubble_sort(lst):
    if len(lst) < 2:
        return

    # 最后一次交换的下标， 每经过一次便利，后面有序区至少多增加一位
    last_change_index = len(lst) - 1

    for i in range(len(lst) - 1):
        print(i, last_change_index)
        # 标记在一轮遍历中是否发生了交换，如果一次也没有发生交换，则元素已经整体有序
        is_change = False
        for j in range(last_change_index):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                last_change_index = j
                is_change = True
        print(lst)
        if is_change is False:
            break


if __name__ == '__main__':
    # lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    lst = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    bubble_sort(lst)
    print(lst)
