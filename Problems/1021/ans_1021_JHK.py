# https://www.acmicpc.net/problem/1021


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class RingDeque:
    def __init__(self, num):
        dummy = Node(-1)
        self.dummy = dummy
        dummy.next = dummy
        dummy.prev = dummy
        self.number = 0
        self.count = 0
        for i in range(1, num + 1):
            self.push_back(i)

    def push_back(self, data):
        newNode = Node(data)
        orgNode = self.dummy.prev
        self.dummy.prev = newNode
        newNode.next = self.dummy
        orgNode.next = newNode
        newNode.prev = orgNode
        self.number += 1

    def push_front(self, data):
        newNode = Node(data)
        orgNode = self.dummy.next
        self.dummy.next = newNode
        newNode.prev = self.dummy
        orgNode.prev = newNode
        newNode.next = orgNode
        self.number += 1

    def pop_front(self):
        point = self.dummy.next
        nextpoint = point.next
        self.dummy.next = nextpoint
        nextpoint.prev = self.dummy
        self.number -= 1
        return point.data

    def pop_back(self):
        point = self.dummy.prev
        nextpoint = point.prev
        self.dummy.prev = nextpoint
        nextpoint.next = self.dummy
        self.number -= 1
        return point.data

    def moveNorm(self):
        # move right
        self.push_front(self.pop_back())

    def moveReverse(self):
        # move left
        self.push_back(self.pop_front())

    def search(self, data):
        cnt = 0
        frontNode = self.dummy.next
        backNode = self.dummy
        while True:
            if frontNode.data == data:
                self.count += cnt
                return True, cnt
            if backNode.data == data:
                self.count += cnt
                return False, cnt
            frontNode = frontNode.next
            backNode = backNode.prev
            cnt += 1

    def minMove_and_Pop(self, data):
        dir, cnt = self.search(data)
        if dir:
            for _ in range(cnt):
                self.moveReverse()
        else:
            for _ in range(cnt):
                self.moveNorm()
        self.pop_front()

    def result(self):
        return self.count


def solve():
    N, _ = map(int, input().split())
    data = list(map(int, input().split()))
    D = RingDeque(N)
    for d in data:
        D.minMove_and_Pop(d)
    print(D.result())
    return


if __name__ == "__main__":
    solve()
