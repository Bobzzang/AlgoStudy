# https://www.acmicpc.net/problem/20923

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
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

    def enqueue_backward(self, data):
        NewNode = Node(data)
        NewNode.prev = self.tail.prev
        NewNode.next = self.tail
        self.tail.prev.next = NewNode
        self.tail.prev = NewNode
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            TarNode = self.tail.prev
            self.tail.prev = TarNode.prev
            TarNode.prev.next = self.tail
            self.size -= 1
            return TarNode.data
        return 0

    def check_head(self):
        if self.size > 0:
            return self.head.next.data
        return 0

    def append_deque(self, NewDeque: "Deque"):
        while NewDeque.size != 0:
            self.enqueue(NewDeque.dequeue())
        return


def check_result(
    DodoDeque: Deque, SuyeonDeque: Deque, DodoGround: Deque, SuyeonGround: Deque
):
    if DodoDeque.size == 0:
        return True
    if SuyeonDeque.size == 0:
        return True

    DodoResult = DodoGround.check_head()
    SuyeonResult = SuyeonGround.check_head()
    if DodoResult == 5 or SuyeonResult == 5:
        # Dodo Wins
        DodoDeque.append_deque(SuyeonGround)
        DodoDeque.append_deque(DodoGround)
        return False
    if DodoResult + SuyeonResult == 5:
        # Suyeon Wins
        SuyeonDeque.append_deque(DodoGround)
        SuyeonDeque.append_deque(SuyeonGround)
        return False
    # Keep going
    return False


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    DodoDeque = Deque()
    SuyeonDeque = Deque()
    DodoGround = Deque()
    SuyeonGround = Deque()
    for _ in range(N):
        do, su = map(int, input().split())
        DodoDeque.enqueue_backward(do)
        SuyeonDeque.enqueue_backward(su)
    for i in range(M):
        if i % 2 == 0:
            DodoGround.enqueue(DodoDeque.dequeue())
        else:
            SuyeonGround.enqueue(SuyeonDeque.dequeue())
        if check_result(DodoDeque, SuyeonDeque, DodoGround, SuyeonGround):
            break
    if DodoDeque.size == 0:
        print("su")
        return
    if SuyeonDeque.size == 0:
        print("do")
        return
    if DodoDeque.size == SuyeonDeque.size:
        print("dosu")
        return
    if DodoDeque.size > SuyeonDeque.size:
        print("do")
        return
    if SuyeonDeque.size > DodoDeque.size:
        print("su")
        return


if __name__ == "__main__":
    solve()
