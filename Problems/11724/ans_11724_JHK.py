# https://www.acmicpc.net/problem/11724

import sys


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.size = 0
        self.link = []

    def linking(self, linkNum):
        self.link.append(linkNum)
        self.size += 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        if self.size == 0:
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def pop_left(self):
        if self.size == 0:
            return 0
        data = self.head.next.data
        self.head = self.head.next
        self.size -= 1
        return data


def exploreLink(Arr, idx, que):
    if Arr[idx].visited:
        return 0
    Arr[idx].visited = True
    LinkList = Arr[idx].link
    for l in LinkList:
        if Arr[l].visited == False:
            que.push(l)
    return 1


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Arr = [GraphNode(x) for x in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        Arr[x].linking(y)
        Arr[y].linking(x)
    que = Queue()
    cnt = 0
    for i in range(1, N + 1):
        cnt += exploreLink(Arr, i, que)
        while que.size != 0:
            exploreLink(Arr, que.pop_left(), que)
    print(cnt)
    return


if __name__ == "__main__":
    solve()
