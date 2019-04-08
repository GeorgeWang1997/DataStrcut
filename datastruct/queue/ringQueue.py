# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: ringQueue.py
@time: 2019-04-07 21:35
"""


class RingQueue:

    def __init__(self, length):
        self.queue = [None]*length
        self.length = length
        self.count = 0
        self.front = 0
        self.rear = 0

    def in_queue(self, element):
        if self.count < self.length:
            self.queue[self.rear] = element
            self.count += 1
            self.rear = self.rear+1 if self.rear+1 < self.length else 0
        else:
            print("队列已满")

    def out_queue(self):
        if self.is_empty():
            return False
        else:
            self.queue[self.front] = None
            self.count -= 1
            if self.front < self.length:
                self.front += 1
            else:
                self.front = 0

    def is_empty(self):
        if self.count == 0:
            return True

    def front_queue(self):
        if self.is_empty():
            return False
        else:
            return self.queue[self.front]


if __name__ == '__main__':
    ringQueue = RingQueue(5)
    ringQueue.in_queue(1)
    ringQueue.in_queue(2)
    ringQueue.in_queue(3)
    ringQueue.in_queue(4)
    ringQueue.in_queue(5)
    ringQueue.in_queue(3)
    ringQueue.out_queue()
    ringQueue.out_queue()
    ringQueue.in_queue(6)
    ringQueue.out_queue()
    ringQueue.in_queue(7)
    print(ringQueue.front_queue(), ringQueue.front, ringQueue.rear)
    print(ringQueue.queue)
