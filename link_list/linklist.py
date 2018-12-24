# -*- coding: utf-8 -*-
# __author: ward
# data: 2018/12/24
# @File: linklist


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# 链表的实现：带头节点的链表 不带头节点的链表

# 带头节点的链表

# 头插法
def create_link_list_head(li):
    head = Node(None)
    for num in li:
        p = Node(num)
        p.next = head.next
        head.next = p
    return head


# 尾插法
def create_link_list_tail(li):
    head = Node(None)
    tail = head
    for num in li:
        p = Node(num)
        tail.next = p
        tail = p
    return head


# 打印输出
def traverse_link_list(head):
    p = head.next
    while p:
        print(p.data)
        p = p.next


# head = create_link_list_head([1, 2, 3, 4, 5])
# head = create_link_list_tail([1, 2, 3, 4, 5])
# traverse_link_list(head)


# 不带头节点的链表

# 头插法
def create_link_list_head2(li):
    head = None
    for num in li:
        p = Node(num)
        p.next = head
        head = p
    return head


# 尾插法
def create_link_list_tail2(li):
    head = None
    tail = head
    for num in li:
        p = Node(num)
        if tail:
            tail.next = p
            tail = p
        else:
            tail = p
            head = p
    return head


# 打印
def traverse_link_list2(head):
    p = head
    while p:
        print(p.data)
        p = p.next


head = create_link_list_head2([1, 2, 3, 4, 5])
head = create_link_list_tail2([1, 2, 3, 4, 5])
traverse_link_list2(head)
