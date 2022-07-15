# https://www.acmicpc.net/problem/5397

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

    def put_left(self, data):
        NewNode = Node(data)
        NewNode.next = self.head.next
        self.head.next.prev = NewNode
        self.head.next = NewNode
        NewNode.prev = self.head
        self.size += 1
        return

    def put_right(self, data):
        NewNode = Node(data)
        NewNode.prev = self.tail.prev
        self.tail.prev.next = NewNode
        self.tail.prev = NewNode
        NewNode.next = self.tail
        self.size += 1
        return

    def pop_left(self):
        if self.size != 0:
            TarNode = self.head.next
            data = TarNode.data
            self.head.next = TarNode.next
            TarNode.next.prev = self.head
            self.size -= 1
            return data
        return 0

    def pop_right(self):
        if self.size != 0:
            TarNode = self.tail.prev
            data = TarNode.data
            self.tail.prev = TarNode.prev
            TarNode.prev.next = self.tail
            self.size -= 1
            return data
        return 0


class InputForm:
    def __init__(self):
        self.LeftDeq = Deque()
        self.RightDeq = Deque()

    def get_input(self, s):
        for c in s:
            if c == "<":
                data = self.LeftDeq.pop_right()
                if data != 0:
                    self.RightDeq.put_left(data)
            elif c == ">":
                data = self.RightDeq.pop_left()
                if data != 0:
                    self.LeftDeq.put_right(data)
            elif c == "-":
                self.LeftDeq.pop_right()
            else:
                self.LeftDeq.put_right(c)

    def print_password(self):
        res = []
        while self.LeftDeq.size != 0:
            res.append(self.LeftDeq.pop_left())
        while self.RightDeq.size != 0:
            res.append(self.RightDeq.pop_left())

        print("".join(res))


def print_password(Log):
    f = InputForm()
    f.get_input(Log)
    f.print_password()


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = [input().rstrip() for _ in range(N)]
    for s in TC:
        print_password(s)
    return


if __name__ == "__main__":
    solve()
