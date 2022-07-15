# https://www.acmicpc.net/problem/3986


import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        self.size += 1

    def pop(self):
        if self.head == None:
            return None
        if self.head.next == None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def top(self):
        if self.head == None:
            return None
        return self.head.data

    def isempty(self):
        return self.size == 0


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = []
    for _ in range(N):
        TC.append(input().rstrip())

    cnt = 0
    for s in TC:
        GoodWordStack = Stack()
        for c in s:
            if GoodWordStack.top() == c:
                GoodWordStack.pop()
            else:
                GoodWordStack.push(c)
        if GoodWordStack.isempty():
            cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
