# https://www.acmicpc.net/problem/12034

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def enqueue(self, data):
        NewNode = Node(data)
        self.head.next.prev = NewNode
        self.head.next = NewNode
        NewNode.next = self.head.next
        NewNode.prev = self.head
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return 0
        TargetNode = self.tail.prev
        self.tail.prev = TargetNode.prev
        TargetNode.prev.next = self.tail
        self.size -= 1
        return TargetNode.data

    def get_last(self):
        if self.size == 0:
            return 0
        TargetNode = self.tail.prev
        return TargetNode.data


def solve():
    input = sys.stdin.readline
    T = int(input())
    TestCases = []
    for _ in range(T):
        N = int(input())
        TestCases.append(list(map(int, input().split())))

    res = []
    for TC in TestCases:
        Que = Queue()
        r = []
        for P in TC:
            if Que.get_last() // 3 * 4 == P:
                r.append(Que.dequeue())
            else:
                Que.enqueue(P)
        res.append(r)

    i = 1
    for r in res:
        print(f"Case #{i}: ", end="")
        print(*r)
        i += 1
    return


if __name__ == "__main__":
    solve()
