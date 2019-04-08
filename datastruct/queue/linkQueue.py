# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: linkQueue.py
@time: 2019-04-07 21:20
"""


class QueueNode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue:
    def __init__(self):
        node = QueueNode()
        self.front = node
        self.rear = node

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def in_queue(self, element):
        node = QueueNode()
        node.data = element
        self.rear.next = node
        self.rear = node

    def out_queue(self):
        if self.is_empty():
            print("队列为空")
            return
        else:
            node = self.front.next
            self.front.next = node.next
            if self.rear == node:
                self.rear = self.front
            return node.data

    def front_queue(self):
        if self.is_empty():
            print("队列为空")
            return
        else:
            return self.front.next.data


if __name__ == '__main__':

    queue = LinkQueue()
    queue.in_queue(1)
    queue.in_queue(2)
    queue.in_queue(3)
    print(queue.out_queue())
    print(queue.out_queue())
    print(queue.out_queue())
    print(queue.out_queue())
