# https://www.acmicpc.net/problem/11866


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircleList:
    def __init__(self):
        dummy = Node(-1)
        self.head = dummy
        self.tail = dummy
        self.current = self.head
        self.number = 0

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = self.head.next
        self.number += 1

    def size(self):
        return self.number

    def countPop(self, idx):
        for i in range(idx - 1):
            self.current = self.current.next
        beforeNode = self.current
        self.current = self.current.next
        beforeNode.next = self.current.next
        self.number -= 1
        return self.current.data


def solve():
    N, K = map(int, input().split())
    ll = CircleList()
    for i in range(1, N + 1):
        ll.append(i)
    ans = []
    while ll.size() != 0:
        ans.append(ll.countPop(K))
    print("<", end="")
    print(", ".join(str(x) for x in ans), end="")
    print(">")

    return


if __name__ == "__main__":
    solve()
