# https://www.acmicpc.net/problem/2164


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        dummy = Node(-1)
        self.head = dummy
        self.tail = dummy
        self.number = 0

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.number += 1

    def round(self):
        self.tail.next = self.head.next
        self.head.next = self.head.next.next
        self.tail = self.tail.next
        self.tail.next = None

    def pop(self):
        self.head.next = self.head.next.next
        self.number -= 1

    def size(self):
        return self.number

    def front(self):
        return self.head.next.data


def solve():
    N = int(input())
    queue = Queue()
    for i in range(1, N + 1):
        queue.append(i)
    while queue.size() != 1:
        queue.pop()
        queue.round()

    print(queue.front())
    return


if __name__ == "__main__":
    solve()
