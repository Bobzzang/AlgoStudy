# https://www.acmicpc.net/problem/2178

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
        getNode = self.head.next
        if getNode.next is None:
            self.tail = self.head
            self.head.next = self.head
        else:
            self.head.next = getNode.next
        return getNode.data


def bfs(maze, M, N, que: Queue):
    x = 0
    y = 0
    depth = 1
    que.set([x, y, depth])
    maze[y][x] = 0
    while True:
        x, y, depth = que.get()
        if x == M - 1 and y == N - 1:
            return depth
        if x > 0:
            if maze[y][x - 1] == 1:
                que.set([x - 1, y, depth + 1])
                maze[y][x - 1] = 0
        if x < M - 1:
            if maze[y][x + 1] == 1:
                que.set([x + 1, y, depth + 1])
                maze[y][x + 1] = 0
        if y > 0:
            if maze[y - 1][x] == 1:
                que.set([x, y - 1, depth + 1])
                maze[y - 1][x] = 0
        if y < N - 1:
            if maze[y + 1][x] == 1:
                que.set([x, y + 1, depth + 1])
                maze[y + 1][x] = 0


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    que = Queue()
    print(bfs(maze, M, N, que))
    return


if __name__ == "__main__":
    solve()
