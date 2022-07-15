# https://www.acmicpc.net/problem/5430


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.reverse = False
        self.size = 0
        self.errorSet = False

    def push(self, data):
        newNode = Node(data)
        oldNode = self.tail.prev
        oldNode.next = newNode
        newNode.prev = oldNode
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1

    def revert(self):
        self.reverse ^= True

    def pop_front(self):
        if self.size > 0:
            oldHead = self.head.next
            nextHead = oldHead.next
            self.head.next = nextHead
            nextHead.prev = self.head
            self.size -= 1
            return oldHead.data
        else:
            return -1

    def pop_back(self):
        if self.size > 0:
            oldTail = self.tail.prev
            nextTail = oldTail.prev
            self.tail.prev = nextTail
            nextTail.next = self.tail
            self.size -= 1
            return oldTail.data
        else:
            return -1

    def delete(self):
        if self.reverse:
            temp = self.pop_back()
        else:
            temp = self.pop_front()

        if temp < 0:
            self.errorSet = True

    def printAll(self):
        res = []
        while True:
            if self.reverse:
                res.append(self.pop_back())
            else:
                res.append(self.pop_front())
            if res[-1] < 0:
                res.pop()
                break
        if self.errorSet:
            print("error")
        else:
            print("[", end="")
            print(",".join(str(x) for x in res), end="")
            print("]")


def solve():
    N = int(input())
    TC = []
    for _ in range(N):
        cmd = input()
        input()  # 안쓰는 input
        temp = input().replace(",", " ").replace("[", "").replace("]", "")
        data = list(map(int, temp.split()))
        TC.append([cmd, data])

    for t in TC:
        deque = Deque()
        cmd, data = t
        for d in data:
            deque.push(d)
        for c in cmd:
            if c == "R":
                deque.revert()
            else:
                deque.delete()
        deque.printAll()

    return


if __name__ == "__main__":
    solve()
