# https://www.acmicpc.net/problem/5002


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head.next
        self.head.next = NewNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 0
        self.size -= 1
        TarNode = self.head.next
        self.head.next = TarNode.next
        TarNode.next = None
        return TarNode.data

    def check_top(self):
        if self.size == 0:
            return 0
        return self.head.next.data

    def check_second(self):
        if self.size < 2:
            return 0
        return self.head.next.next.data

    def is_remain(self):
        if self.size == 0:
            return False
        return True


def solve():
    X = int(input())
    People = input()
    Lines = Stack()
    for p in People[::-1]:
        if p == "W":
            Lines.push(1)
        else:
            Lines.push(-1)

    totalCnt = 0
    diffCnt = 0
    while Lines.is_remain():
        if Lines.size == 1:
            first = Lines.pop()
            diffCnt += first
            if diffCnt <= X and diffCnt >= -X:
                totalCnt += 1
            print(totalCnt)
            return

        else:
            first = Lines.pop()
            second = Lines.pop()
            is_same = first * second > 0

            if diffCnt == 0:
                diffCnt += first
                totalCnt += 1
                Lines.push(second)
                continue

            if diffCnt * first < 0:
                diffCnt += first
                totalCnt += 1
                Lines.push(second)
                continue

            if diffCnt * second < 0:
                diffCnt += second
                totalCnt += 1
                Lines.push(first)
                continue

            if abs(diffCnt) == X:
                print(totalCnt)
                return
            else:
                diffCnt += first
                totalCnt += 1
                Lines.push(second)
                continue

    return


if __name__ == "__main__":
    solve()
