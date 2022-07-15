# https://www.acmicpc.net/problem/1325

# DFS로는 시간초과가 난다. DFS로 성공하는 풀이를 못찾음.. 다풀었는데...

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
        OldTop = self.head.next
        OldTop.prev = NewNode
        NewNode.next = OldTop
        self.head.next = NewNode
        NewNode.prev = self.head
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            Target = self.tail.prev
            data = Target.data
            self.tail.prev = Target.prev
            Target.prev.next = self.tail
            self.size -= 1
            del Target
            return data
        return 0

    def get_size(self):
        return self.size


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Coms = [[] for _ in range(N + 1)]
    for _ in range(M):
        LinkA, LinkB = map(int, input().split())
        Coms[LinkB].append(LinkA)

    queue = Queue()
    MaxLink = 0
    MaxLinkComs = []

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True
        queue.enqueue(i)

        cnt = 0
        while queue.get_size() > 0:
            j = queue.dequeue()
            cnt += 1
            for c in Coms[j]:
                if visited[c] == False:
                    visited[c] = True
                    queue.enqueue(c)

        if cnt > MaxLink:
            MaxLink = cnt
            MaxLinkComs.clear()
            MaxLinkComs.append(i)
        elif cnt == MaxLink:
            MaxLinkComs.append(i)

    print(*MaxLinkComs)
    return


if __name__ == "__main__":
    solve()
