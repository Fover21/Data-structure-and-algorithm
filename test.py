# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/25
# @File: test


# s = iter([1, 2, 3])
# print(s.__next__())

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# 头插法 （带头节点的方式）
def create(li):
    head = Node(None)
    for num in li:
        p = Node(num)
        p.next = head.next
        head.next = p
    return head


# 计算链表的长度
def size(head):
    count = 0
    p = head.next
    while p:
        count += 1
        p = p.next
    return count


# 查询链表中元素
def search(head, item):
    current = head
    found = False
    while current and not found:
        if current.data == item:
            found = True
        else:
            current = current.next
    return found


# 删除链表中元素
def remove(head, item):
    current = head
    previous = None
    found = False
    while not found:
        if current.data == item:
            found = True
        else:
            previous = current
            current = current.next
    previous.next = current.next


# 打印
def print_list(head):
    p = head.next
    while p:
        print(p.data)
        p = p.next


head = create([1, 2, 3, 4, 5])
print_list(head)
# print_list(head)
# print(size(head))
# print(search(head, 11))
print("remove", remove(head, 1))
print_list(head)
