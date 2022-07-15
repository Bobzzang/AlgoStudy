# https://www.acmicpc.net/problem/11279

# heap을 list 이용하여 구현

import sys


class Heap:
    def __init__(self):
        self.data = [0]
        # index 참조 편의를 위해 0 자리를 채움 (바꾸지 않음)

    def push(self, data):
        self.data.append(data)
        targetIdx = len(self.data) - 1
        while targetIdx != 1:
            if self.data[targetIdx] > self.data[targetIdx // 2]:
                self.data[targetIdx], self.data[targetIdx // 2] = (
                    self.data[targetIdx // 2],
                    self.data[targetIdx],
                )
                targetIdx = targetIdx // 2
            else:
                break

    def pop_max(self):
        if len(self.data) == 2:
            return self.data.pop()
        if len(self.data) > 2:
            res = self.data[1]
            self.data[1] = self.data.pop()
            self.heapify(1)
            return res
        return 0

    def heapify(self, index):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        largestValIndex = index
        if len(self.data) > leftIndex:
            # Left leaf 존재
            if self.data[largestValIndex] < self.data[leftIndex]:
                largestValIndex = leftIndex
        if len(self.data) > rightIndex:
            # Right leaf 존재
            if self.data[largestValIndex] < self.data[rightIndex]:
                largestValIndex = rightIndex

        if largestValIndex != index:
            self.data[index], self.data[largestValIndex] = (
                self.data[largestValIndex],
                self.data[index],
            )
            self.heapify(largestValIndex)

    def command(self, cmd):
        if cmd == 0:
            print(self.pop_max())
        else:
            self.push(cmd)


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = []
    H = Heap()
    for _ in range(N):
        TC.append(int(input()))
    for cmd in TC:
        H.command(cmd)

    return


if __name__ == "__main__":
    solve()
