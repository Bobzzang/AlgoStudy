# https://www.acmicpc.net/problem/4949

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        dummy = Node(None)
        self.top = dummy
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top.next
        self.top.next = newNode
        self.size += 1

    def pop(self):
        if self.size > 0:
            # res = self.top.next.data
            self.top.next = self.top.next.next
            self.size -= 1

    def checkTop(self):
        if self.size > 0:
            return self.top.next.data
        return None

    def input(self, data):
        if data == "[" or data == "(":
            self.push(data)
        elif data == "]":
            if self.checkTop() == "[":
                self.pop()
            else:
                self.push(data)
        elif data == ")":
            if self.checkTop() == "(":
                self.pop()
            else:
                self.push(data)

    def getSize(self):
        return self.size


def solve():
    TC = []
    while True:
        temp = input().rstrip()
        if temp == ".":
            break
        TC.append(temp)
    for inpStr in TC:
        stk = Stack()
        for c in inpStr:
            stk.input(c)
        if stk.getSize() == 0:
            print("yes")
        else:
            print("no")
    return


if __name__ == "__main__":
    solve()
