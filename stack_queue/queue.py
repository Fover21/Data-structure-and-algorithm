# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/24
# @File: queue

from collections import deque  # 双端队列

# from queue import Queue  # Queue的实现就是基于deque的

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())
print(q)
q.appendleft(10)
print(q)
q.pop()
print(q)


# 用两个栈实现队列
class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


# 小栗子
q = deque([1, 2, 3, 4, 5], 3)
print(q)  # 返回的是最后三个的数据

# linux中的tail功能，就是通过队列的这个性质来的
