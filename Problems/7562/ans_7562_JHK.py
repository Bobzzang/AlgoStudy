# https://www.acmicpc.net/problem/7562

from ast import Not
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

    def set(self, data):
        NewNode = Node(data)
        self.tail.next = NewNode
        self.tail = NewNode
        self.size += 1

    def get(self):
        targetNode = self.head.next
        if self.size == 1:
            self.tail = self.head
            self.head.next = self.tail
        else:
            self.head.next = targetNode.next
        self.size -= 1
        return targetNode.data


def checkAround(N, defx, defy, movNum, NotVisited, que: Queue):
    # o1o2o
    # 6ooo3
    # oo#oo
    # 7ooo4
    # o6o5o

    # 1
    x = defx - 1
    y = defy - 2
    if x >= 0 and y >= 0 and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 2
    x = defx + 1
    y = defy - 2
    if x < N and y >= 0 and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 3
    x = defx + 2
    y = defy - 1
    if x < N and y >= 0 and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 4
    x = defx + 2
    y = defy + 1
    if x < N and y < N and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 5
    x = defx + 1
    y = defy + 2
    if x < N and y < N and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 6
    x = defx - 1
    y = defy + 2
    if x >= 0 and y < N and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 7
    x = defx - 2
    y = defy + 1
    if x >= 0 and y < N and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])

    # 8
    x = defx - 2
    y = defy - 1
    if x >= 0 and y >= 0 and NotVisited[y][x]:
        NotVisited[y][x] = False
        que.set([x, y, movNum + 1])


def getMovingNum(N, StartPos, EndPos):
    que = Queue()
    NotVisited = [[True] * N for _ in range(N)]
    x, y = StartPos
    movNum = 0
    NotVisited[y][x] = False
    que.set([x, y, movNum])
    while que.size > 0:
        x, y, movNum = que.get()
        if [x, y] == EndPos:
            return movNum
        checkAround(N, x, y, movNum, NotVisited, que)


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    TCSet = []
    for _ in range(TC_NUM):
        N = int(input())
        StartPos = list(map(int, input().split()))
        EndPos = list(map(int, input().split()))
        TCSet.append([N, StartPos, EndPos])

    res = []
    for TC in TCSet:
        N, StartPos, EndPos = TC
        res.append(getMovingNum(N, StartPos, EndPos))

    for r in res:
        print(r)
    return


if __name__ == "__main__":
    solve()
