# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: heapSort.py
@time: 2019-04-13 15:44
"""
"""
首先将数组构建成大顶堆，每个元素的父亲节点的下标值为(index-1)/2，左右孩子节点的下标值分别为
2*index+1，2*index+2，从0号位元素开始插入构建大根堆，只要他比他的父亲节点大就交换位置。构建好
大根堆以后，就进行heapify操作，将index号位元素与最后一个元素交换，因为时大根堆，所以index号位置元素是
最大的元素，然后把0~N-1位置的元素重新构造成大根堆，首先查找index号位置左右孩子节点的最大值，如果不比
index号位置元素大，则直接退出循环，如果比index号位置元素大，则交换，然后将index值改为左右孩子节点值的
最大下标，继续下一次的比较
"""


def heap_sort(lst):
    if len(lst) < 2:
        return

    for i in range(len(lst)):
        heap_insert(lst, i)

    size = len(lst) - 1
    lst[0], lst[size] = lst[size], lst[0]
    while size > 0:
        heapify(lst, 0, size)
        size -= 1
        lst[0], lst[size] = lst[size], lst[0]


def heap_insert(lst, index):
    father_index = int((index-1) / 2)
    while lst[index] > lst[father_index]:
        lst[index], lst[father_index] = lst[father_index], lst[index]
        index = father_index
        father_index = int((index-1) / 2)


def heapify(lst, index, size):
    left = 2 * index + 1
    while left < size:
        largest = [left, left + 1][(left + 1) < size and lst[left] < lst[left + 1]]
        if lst[index] >= lst[largest]:
            break
        lst[index], lst[largest] = lst[largest], lst[index]
        index = largest
        left = 2 * index + 1


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    heap_sort(lst)
    print(lst)
