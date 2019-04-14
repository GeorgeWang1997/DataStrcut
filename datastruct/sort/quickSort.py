# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: quickSort.py
@time: 2019-04-13 15:02
"""
import random

"""
首先随机一个位置的数作为主元，然后将它与最后一个位置的元素进行交换，交换以后将数组进行分区，
小于主元的数放在左边，等于的数放中间，大于的数放右边，分区过程中，默认小于区开始位置less等于left-1，
大于区开始位置more等于right，从left位置元素开始遍历，如果小于主元即right位置上的元素，则将less加一，
然后将left位置元素与less位置元素交换，交换以后将left值加一，开始下一轮比较；如果left位置元素大于主元，
则more加一，然后交换left位置与more位置元素，因为交换以后不知道交换到left位置more位置元素的大小，所以left不变，
继续下一次比较；如果left位置元素等于主元，则left加一，继续一轮比较。当left值等于more值时，停止比较，将right位置
上的元素与more位置上的元素交换，达到小于主元的数放左边，等于放中间，大于放右边
"""


def quick_sort(lst, left, right):
    if len(lst) < 2:
        return

    if left < right:
        pivot = random.randint(left, right)
        lst[pivot], lst[right] = lst[right], lst[pivot]
        border = partition(lst, left, right)
        quick_sort(lst, left, border[0])
        quick_sort(lst, border[1], right)


def partition(lst, left, right):
    less = left - 1
    more = right
    while left < more:
        if lst[left] < lst[right]:
            less += 1
            lst[less], lst[left] = lst[left], lst[less]
            left += 1
        elif lst[left] > lst[right]:
            more -= 1
            lst[left], lst[more] = lst[more], lst[left]
        else:
            left += 1

    lst[more], lst[right] = lst[right], lst[more]
    return [less, more+1]


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    quick_sort(lst, 0, 9)
    print(lst)
