# https://www.acmicpc.net/problem/16953


class Node:
    def __init__(self, data, level):
        self.data = data
        self.level = level
        self.next = None


class Queue:
    # 항상 doubly linked list로 구현했었는데... 뭔가 복잡하네.
    def __init__(self):
        self.size = 0

    def enqueue(self, data, level):
        NewNode = Node(data, level)
        if self.size == 0:
            self.head = NewNode
            self.tail = NewNode
            self.head.next = self.tail
        else:
            self.tail.next = NewNode
            self.tail = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return 0, 0

        data = self.head.data
        level = self.head.level
        self.head = self.head.next
        self.size -= 1

        return data, level

    def is_not_empty(self):
        return self.size > 0


def solve():
    A, B = map(int, input().split())
    queue = Queue()

    cnt = 0
    queue.enqueue(A, 1)
    while queue.is_not_empty():
        data, level = queue.dequeue()
        if data == B:
            print(level)
            return
        if data > B:
            continue
        queue.enqueue(data * 2, level + 1)
        queue.enqueue(data * 10 + 1, level + 1)

    print(-1)
    return


if __name__ == "__main__":
    solve()
