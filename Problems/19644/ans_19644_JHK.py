# https://www.acmicpc.net/problem/19644
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
        NewNode.next = self.head.next
        self.head.next.prev = NewNode
        self.head.next = NewNode
        NewNode.prev = self.head
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        TarNode = self.tail.prev
        data = TarNode.data
        TarNode.prev.next = self.tail
        self.tail.prev = TarNode.prev
        self.size -= 1
        return data

    def check_tail(self):
        if self.size == 0:
            return -1
        TarNode = self.tail.prev
        data = TarNode.data
        return data


def solve():
    input = sys.stdin.readline
    L = int(input())
    ML, MK = map(int, input().split())
    C = int(input())
    Zombies = [int(input()) for _ in range(L)]

    ReduceDmgList = Queue()
    Dmg = 0
    MaxDmg = ML * MK
    for i, zom in enumerate(Zombies):
        if i == ReduceDmgList.check_tail():
            ReduceDmgList.dequeue()
            MaxDmg = min(ML * MK, MaxDmg + MK)
        Dmg = min(MaxDmg, Dmg + MK)
        if zom <= Dmg:
            # Dmg = EstDmg
            continue
        if C > 0:
            Dmg = max(0, Dmg - MK)
            ReduceDmgList.enqueue(i + ML)
            MaxDmg = max(0, MaxDmg - MK)
            C -= 1
            continue
        else:
            print("NO")
            return
    print("YES")
    return


if __name__ == "__main__":
    solve()
