# https://www.acmicpc.net/problem/12789


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(0)

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def pop(self):
        if self.head.data == 0:
            return 0
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self):
        return self.head.data


def solve():
    N = int(input())
    Students = list(map(int, input().split()))
    OrgLine = Stack()
    Students.reverse()
    for s in Students:
        OrgLine.push(s)
    BufferLine = Stack()

    TargetNum = 1
    while TargetNum != N:
        if BufferLine.top() == TargetNum:
            BufferLine.pop()
            TargetNum += 1
            continue
        if OrgLine.top() == TargetNum:
            OrgLine.pop()
            TargetNum += 1
            continue
        if OrgLine.top() == 0 and BufferLine.top() != TargetNum:
            print("Sad")
            return
        BufferLine.push(OrgLine.pop())
    print("Nice")
    return


if __name__ == "__main__":
    solve()
