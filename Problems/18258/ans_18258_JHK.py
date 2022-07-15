# https://www.acmicpc.net/problem/18258

# pypy3으로는 통과하는데, python3로는 안된다...
# python3로 푼 코드들 확인해보니
# 1. collections.deque 패키지 사용
# 2. list로 만들고 pop 위치를 저장 (pop 하면서 리스트 데이터를 삭제하지 않음)

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        dummy = Node(-1)
        self.head = dummy
        self.tail = dummy
        # self.current = None
        # self.before = None
        self.number = 0

    def push(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.number += 1

    def pop(self):
        if self.head == self.tail:
            print(-1)
            return
        print(self.head.next.data)
        self.number -= 1
        if self.head.next == self.tail:
            self.head.next = self.head
            self.tail = self.head
        else:
            self.head.next = self.head.next.next

    def size(self):
        print(self.number)

    def empty(self):
        if self.number == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.head.next == None:
            print(-1)
        else:
            print(self.head.next.data)

    def back(self):
        print(self.tail.data)


def solve():
    input = sys.stdin.readline
    N = int(input())

    queue = Queue()

    for _ in range(N):
        cmd = input().rstrip().split()
        if cmd[0] == "pop":
            queue.pop()
        elif cmd[0] == "size":
            queue.size()
        elif cmd[0] == "empty":
            queue.empty()
        elif cmd[0] == "front":
            queue.front()
        elif cmd[0] == "back":
            queue.back()
        else:  # push
            queue.push(int(cmd[1]))

    return


if __name__ == "__main__":
    solve()
