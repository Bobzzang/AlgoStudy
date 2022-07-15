# https://www.acmicpc.net/problem/1874

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        dummy = Node(0)
        self.head = dummy
        self.size = 0
        self.current = 0
        self.history = []
        self.historyValid = True

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1
        if self.historyValid:
            self.history.append("+")

    def pop(self):
        if self.size == 0:
            self.historyValid = False
            return None
        else:
            res = self.head.next.data
            self.head.next = self.head.next.next
            self.size -= 1
            if self.historyValid:
                self.history.append("-")
            return res

    def autoPush(self):
        self.current += 1
        self.push(self.current)

    def checkCurrent(self):
        return self.current

    def getHistory(self):
        if self.historyValid:
            return self.history
        else:
            return ["NO"]

    def setHistoryInvalid(self):
        self.historyValid = False


def solve():
    input = sys.stdin.readline
    N = int(input())
    InData = []
    s = Stack()
    for _ in range(N):
        InData.append(int(input()))
    for d in InData:
        current = 0
        while True:
            if s.checkCurrent() < d:
                s.autoPush()
            elif s.checkCurrent() == d:
                s.pop()
                break
            else:
                if s.pop() != d:
                    s.setHistoryInvalid()
                break

    result = s.getHistory()
    for r in result:
        print(r)
    return


if __name__ == "__main__":
    solve()
