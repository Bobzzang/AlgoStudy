# https://www.acmicpc.net/problem/1966

import sys


class Node:
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.next = None


class Queue:
    def __init__(self):
        dummy = Node(-1, False)
        self.head = dummy
        self.tail = dummy

    def append(self, data, target=False):
        newNode = Node(data, target)
        self.tail.next = newNode
        self.tail = newNode

    def max(self):
        point = self.head
        maxval = 0
        while point.next != None:
            point = point.next
            if maxval < point.data:
                maxval = point.data
        return maxval

    def pend(self):
        point = self.head.next
        self.head.next = point.next
        self.tail.next = point
        self.tail = point
        point.next = None

    def print(self):
        point = self.head.next
        self.head.next = point.next
        self.cnt += 1

    def checkFirst(self):
        return self.head.next.data, self.head.next.target

    def printDocs(self):
        self.cnt = 1
        while True:
            P, Tar = self.checkFirst()
            if P >= self.max():
                if Tar:
                    return self.cnt
                else:
                    self.print()
            else:
                self.pend()


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    TC = []
    for _ in range(TC_NUM):
        N, M = map(int, input().split())
        Priority = list(map(int, input().split()))
        TC.append([M, Priority])

    for T in TC:
        M, docs = T
        queue = Queue()
        for i, d in enumerate(docs):
            if i == M:
                queue.append(d, True)
            else:
                queue.append(d)
        print(queue.printDocs())
    return


if __name__ == "__main__":
    solve()
