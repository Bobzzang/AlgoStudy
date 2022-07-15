# https://www.acmicpc.net/problem/17086

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


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
        self.head.next.prev = NewNode
        NewNode.prev = self.head
        self.head.next = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        TarNode = self.tail.prev
        self.tail.prev = TarNode.prev
        TarNode.prev.next = self.tail
        TarNode.prev = None
        TarNode.next = None
        self.size -= 1
        return TarNode.data


def set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY):
    if TargetX >= 0 and TargetX <= M - 1 and TargetY >= 0 and TargetY <= N - 1:
        TargetIdx = TargetY * M + TargetX
        if is_visited[TargetIdx] == False:
            if SharkMap[TargetIdx] == 0 or SharkMap[TargetIdx] > Level + 1:
                ExploreQueue.enqueue(TargetIdx)
                SharkMap[TargetIdx] = Level + 1
            else:
                is_visited[TargetIdx] = True


def save_safe_dist(i, SharkMap, is_visited, ExploreQueue, N, M):
    ExploreQueue.enqueue(i)
    while ExploreQueue.size != 0:
        BaseIdx = ExploreQueue.dequeue()
        is_visited[BaseIdx] = True
        Level = SharkMap[BaseIdx]

        BaseX, BaseY = BaseIdx % M, BaseIdx // M

        TargetX, TargetY = BaseX - 1, BaseY - 1
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX - 1, BaseY
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX - 1, BaseY + 1
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX, BaseY - 1
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX, BaseY + 1
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX + 1, BaseY - 1
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX + 1, BaseY
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

        TargetX, TargetY = BaseX + 1, BaseY + 1
        set_Queue(SharkMap, is_visited, ExploreQueue, N, M, Level, TargetX, TargetY)

    return


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    SharkMap = []
    for _ in range(N):
        SharkMap += list(map(int, input().split()))
    ExploreQueue = Queue()
    for i, v in enumerate(SharkMap):
        is_visited = [False] * len(SharkMap)
        if v == 1:
            save_safe_dist(i, SharkMap, is_visited, ExploreQueue, N, M)
    print(max(SharkMap) - 1)
    return


if __name__ == "__main__":
    solve()
