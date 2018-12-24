# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/24
# @File: stack


# 列表实现栈
class MyStack(object):

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return self.data == []

    def size(self):
        return len(self.data)


stack = MyStack()
stack.push(9)
stack.push(9)
print(stack)
print(stack.top())
print(stack.pop())
print(stack)


# 例子（括号匹配）
def bracket_match(s):
    stack = []
    d = {"}": "{", ']': '[', ')': ')'}
    for ch in s:
        if ch in {'{', '[', '('}:
            stack.append(ch)
        elif len(stack) == 0:
            print('缺少左括号')
        elif d[ch] == stack[-1]:
            stack.pop()
        else:
            print('左右括号不匹配')
            return False
    if len(stack) > 0:
        print('缺少右括号')
        return False
    else:
        return True


# print(bracket_match("[(])"))

import queue

stack = queue.LifoQueue()  # 可看LifoQueue的源码，就是以上原理
stack.put(1)
stack.put(2)
print(stack.get())
print(stack.queue)
print(stack.qsize())
# stack.empty()  # 栈空
# stack.full()  # 栈满

