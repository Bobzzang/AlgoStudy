# https://www.acmicpc.net/problem/11286

import sys


class Heap:
    def __init__(self):
        self.data = [0]
        self.size = 0

    def push(self, data):
        self.data.append(data)
        self.size += 1
        child = self.size
        while child != 1:
            parent = child // 2

            if self.absBigger(parent, child):
                self.data[parent], self.data[child] = (
                    self.data[child],
                    self.data[parent],
                )
                child = parent
            else:
                break

    def pop(self):
        if self.size > 1:
            res = self.data[1]
            self.data[1] = self.data.pop()
            self.size -= 1
            self.heapify(1)
            return res
        elif self.size == 1:
            self.size -= 1
            return self.data.pop()
        else:
            return 0

    def absBigger(self, idx1, idx2):
        if self.data[idx1] > 0:
            data1 = self.data[idx1]
        else:
            data1 = -self.data[idx1]
        if self.data[idx2] > 0:
            data2 = self.data[idx2]
        else:
            data2 = -self.data[idx2]

        if data1 > data2:
            return True
        elif data1 == data2:
            if self.data[idx1] < 0:
                return False
            elif self.data[idx2] < 0:
                return True
        return False

    def heapify(self, idx):
        while True:
            left = idx * 2
            right = idx * 2 + 1
            smallest = idx
            if self.size >= left and self.absBigger(smallest, left):
                smallest = left
            if self.size >= right and self.absBigger(smallest, right):
                smallest = right

            if idx != smallest:
                self.data[smallest], self.data[idx] = (
                    self.data[idx],
                    self.data[smallest],
                )
                idx = smallest
            else:
                break

    def run(self, cmd):
        if cmd == 0:
            print(self.pop())
        else:
            self.push(cmd)


def solve():
    input = sys.stdin.readline
    N = int(input())
    H = Heap()
    for _ in range(N):
        H.run(int(input()))
    return


if __name__ == "__main__":
    solve()
