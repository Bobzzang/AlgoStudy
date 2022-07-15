# https://www.acmicpc.net/problem/2841

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(-1)
        self.size = 0

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        self.size += 1

    def pop(self):
        if self.head.data == -1:
            return -1
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def top(self):
        return self.head.data


def solve():
    input = sys.stdin.readline
    N, P = map(int, input().split())
    TC = []
    for _ in range(N):
        Line, Prat = map(int, input().split())
        TC.append([Line - 1, Prat])

    cnt = 0
    Strings = [Stack() for _ in range(6)]
    for t in TC:
        Line, Prat = t
        while Strings[Line].top() != Prat:
            if Strings[Line].top() < Prat:
                Strings[Line].push(Prat)
                cnt += 1
            else:
                while Strings[Line].top() > Prat:
                    Strings[Line].pop()
                    cnt += 1
                if Strings[Line].top() != Prat:
                    Strings[Line].push(Prat)
                    cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
