# https://www.acmicpc.net/problem/1697

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

    def set(self, data):
        NewNode = Node(data)
        self.tail.next = NewNode
        self.tail = NewNode

    def get(self):
        # if self.head.next.data == None:
        #     return -1
        targetNode = self.head.next
        data = targetNode.data
        if targetNode.next == None:
            self.head.next = self.head
            self.tail = self.head
        else:
            self.head.next = targetNode.next
        return data


def bfs(N, K, que: Queue, NotVisited: list):
    depth = 0
    NotVisited[N] = False
    que.set([N, depth])
    while True:
        N, depth = que.get()
        if N == K:
            print(depth)
            return
        if N - 1 >= 0 and NotVisited[N - 1]:
            NotVisited[N - 1] = False
            que.set([N - 1, depth + 1])

        if N + 1 < len(NotVisited) and NotVisited[N + 1]:
            NotVisited[N + 1] = False
            que.set([N + 1, depth + 1])

        if N * 2 < len(NotVisited) and NotVisited[N * 2]:
            NotVisited[N * 2] = False
            que.set([N * 2, depth + 1])


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    NotVisited = [True] * (max(K * 2, N) + 1)
    que = Queue()
    bfs(N, K, que, NotVisited)
    return


if __name__ == "__main__":
    solve()
