# https://www.acmicpc.net/problem/1926

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
        NewNode.next = self.head.next
        NewNode.prev = self.head
        self.head.next.prev = NewNode
        self.head.next = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        self.size -= 1
        TargetNode = self.tail.prev
        self.tail.prev = TargetNode.prev
        TargetNode.prev.next = self.tail
        TargetNode.next = None
        TargetNode.prev = None
        return TargetNode.data


def explore_paint(N, M, Paint, is_visited, VisitQueue):
    VisitIdx = VisitQueue.dequeue()
    x, y = VisitIdx % M, VisitIdx // M
    if x != 0:
        if Paint[VisitIdx - 1] == 1 and is_visited[VisitIdx - 1] == False:
            VisitQueue.enqueue(VisitIdx - 1)
            is_visited[VisitIdx - 1] = True
    if x != M - 1:
        if Paint[VisitIdx + 1] == 1 and is_visited[VisitIdx + 1] == False:
            VisitQueue.enqueue(VisitIdx + 1)
            is_visited[VisitIdx + 1] = True
    if y != 0:
        if Paint[VisitIdx - M] == 1 and is_visited[VisitIdx - M] == False:
            VisitQueue.enqueue(VisitIdx - M)
            is_visited[VisitIdx - M] = True
    if y != N - 1:
        if Paint[VisitIdx + M] == 1 and is_visited[VisitIdx + M] == False:
            VisitQueue.enqueue(VisitIdx + M)
            is_visited[VisitIdx + M] = True
    return


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Paint = []
    for _ in range(N):
        Paint += list(map(int, input().split()))
    is_visited = [False] * len(Paint)
    cnt = 0
    VisitQueue = Queue()
    MaxPaintSize = 0
    for i in range(len(Paint)):
        if Paint[i] == 1 and is_visited[i] == False:
            cnt += 1
            VisitQueue.enqueue(i)
            is_visited[i] = True
        PaintSize = 0
        while VisitQueue.size != 0:
            explore_paint(N, M, Paint, is_visited, VisitQueue)
            PaintSize += 1
        MaxPaintSize = max(MaxPaintSize, PaintSize)
    print(cnt)
    print(MaxPaintSize)
    return


if __name__ == "__main__":
    solve()
