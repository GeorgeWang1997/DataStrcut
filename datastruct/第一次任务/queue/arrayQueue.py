# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: arrayQueue.py
@time: 2019-04-07 21:03
"""


class ArrayQueue:

    def __init__(self, length):
        self.queue = [None]*length
        self.length = length
        self.front = 0
        self.rear = 0

    def in_queue(self, element):
        if self.rear < self.length:
            self.queue[self.rear] = element
            self.rear += 1
        else:
            print("队列已满")

    def out_queue(self):
        if self.is_empty():
            return False
        else:
            self.queue[self.front] = None
            self.front += 1

    def is_empty(self):
        if self.front == self.rear:
            return True

    def front_queue(self):
        if self.is_empty():
            return False
        else:
            return self.queue[self.front]


if __name__ == '__main__':
    arrayQueue = ArrayQueue(5)
    arrayQueue.in_queue(1)
    arrayQueue.in_queue(2)
    arrayQueue.in_queue(3)
    arrayQueue.out_queue()
    arrayQueue.out_queue()
    print(arrayQueue.front_queue(), arrayQueue.front, arrayQueue.rear)
    print(arrayQueue.queue)
