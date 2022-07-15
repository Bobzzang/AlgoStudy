# https://www.acmicpc.net/problem/10866

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.number = 0

    def push_front(self, data):
        newNode = Node(data)
        orgNode = self.head.next
        newNode.next = orgNode
        orgNode.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head
        self.number += 1

    def push_back(self, data):
        newNode = Node(data)
        orgNode = self.tail.prev
        newNode.prev = orgNode
        orgNode.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        self.number += 1

    def pop_front(self):
        if self.number > 0:
            point = self.head.next
            point2 = point.next
            self.head.next = point2
            point2.prev = self.head
            self.number -= 1
            print(point.data)
        else:
            print(-1)

    def pop_back(self):
        if self.number > 0:
            point = self.tail.prev
            point2 = point.prev
            self.tail.prev = point2
            point2.next = self.tail
            self.number -= 1
            print(point.data)
        else:
            print(-1)

    def size(self):
        print(self.number)

    def empty(self):
        if self.number == 0:
            print(1)
        else:
            print(0)

    def front(self):
        print(self.head.next.data)

    def back(self):
        print(self.tail.prev.data)


def solve():
    input = sys.stdin.readline
    N = int(input())
    d = Deque()
    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "pop_front":
            d.pop_front()
        elif cmd[0] == "pop_back":
            d.pop_back()
        elif cmd[0] == "size":
            d.size()
        elif cmd[0] == "empty":
            d.empty()
        elif cmd[0] == "front":
            d.front()
        elif cmd[0] == "back":
            d.back()
        elif cmd[0] == "push_front":
            d.push_front(int(cmd[1]))
        else:
            d.push_back(int(cmd[1]))

    return


if __name__ == "__main__":
    solve()
