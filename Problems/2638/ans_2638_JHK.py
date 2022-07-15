# https://www.acmicpc.net/problem/2638

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.head.next = self.tail
        self.size = 0

    def enqueue(self, data):
        NewNode = Node(data)
        self.tail.next = NewNode
        self.tail = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return 0
        if self.size == 1:
            self.size -= 1
            data = self.tail.data
            self.tail = self.head
            self.head.next = self.tail
            return data
        data = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return data


def set_outer_atmos(Cheese, pos, N, M):
    AtmoList = [pos]
    while len(AtmoList) != 0:
        i, j = AtmoList.pop()
        Cheese[i * M + j] = 2
        if i > 0 and Cheese[(i - 1) * M + j] == 0:
            AtmoList.append((i - 1, j))
        if j > 0 and Cheese[i * M + j - 1] == 0:
            AtmoList.append((i, j - 1))
        if i < N - 1 and Cheese[(i + 1) * M + j] == 0:
            AtmoList.append((i + 1, j))
        if j < M - 1 and Cheese[i * M + j + 1] == 0:
            AtmoList.append((i, j + 1))
    return


def check_around(Cheese, pos, N, M):
    i, j = pos
    cnt = 0
    if i > 0:
        if Cheese[(i - 1) * M + j] == 2:
            cnt += 1
    if j > 0:
        if Cheese[i * M + j - 1] == 2:
            cnt += 1
    if i < N - 1:
        if Cheese[(i + 1) * M + j] == 2:
            cnt += 1
    if j < M - 1:
        if Cheese[i * M + j + 1] == 2:
            cnt += 1
    return cnt > 1


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Cheese = []
    for _ in range(N):
        Cheese += list(map(int, input().split()))
    set_outer_atmos(Cheese, (0, 0), N, M)
    CheeseQueue = Queue()
    for i in range(N):
        for j in range(M):
            if Cheese[i * M + j] == 1:
                CheeseQueue.enqueue((i, j))
    cnt = 0
    BufferQueue = Queue()
    while CheeseQueue.size != 0:
        TargetList = []
        while CheeseQueue.size != 0:
            pos = CheeseQueue.dequeue()
            if check_around(Cheese, pos, N, M):
                TargetList.append(pos)
            else:
                BufferQueue.enqueue(pos)
        for target in TargetList:
            set_outer_atmos(Cheese, target, N, M)
        BufferQueue, CheeseQueue = CheeseQueue, BufferQueue
        cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
