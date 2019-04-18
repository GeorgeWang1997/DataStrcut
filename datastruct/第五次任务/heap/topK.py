# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: topK.py
@time: 2019-04-18 22:25
"""


def top_k(lst, k):
    k_min_heap = lst[:k]
    for i in range(k):
        min_heap(k_min_heap, i)

    for item in lst[k:]:
        if item > k_min_heap[0]:
            k_min_heap[0] = item
            heapify(k_min_heap, 0, k)

    return k_min_heap


def min_heap(lst, index):
    father_index = int((index - 1) / 2)
    while lst[index] < lst[father_index]:
        lst[index], lst[father_index] = lst[father_index], lst[index]
        index = father_index
        father_index = int((index - 1) / 2)


def heapify(lst, index, size):
    left = 2 * index + 1
    while left < size:
        litter = [left, left + 1][(left + 1) < size and lst[left] > lst[left + 1]]
        if lst[index] <= lst[litter]:
            break
        lst[index], lst[litter] = lst[litter], lst[index]
        index = litter
        left = 2 * index + 1


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    print(top_k(lst, 3))
