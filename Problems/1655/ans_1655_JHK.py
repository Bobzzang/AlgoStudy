# https://www.acmicpc.net/problem/1655

import sys


class Heap:
    def __init__(self):
        self.data = [0]
        self.size = 0

    def push(self, data):
        self.size += 1
        self.data.append(data)
        target = self.size
        while target != 1 and self.priorChk(target):
            target = target // 2

    def top(self):
        return self.data[1]

    def replace_top(self, data):
        res = self.data[1]
        self.data[1] = data
        self.heapify(1)
        return res


class MaxHeap(Heap):
    def heapify(self, idx):
        while idx <= self.size // 2:
            leftLeaf = idx * 2
            rightLeaf = idx * 2 + 1
            bigest = idx
            if self.size >= leftLeaf and self.data[bigest] < self.data[leftLeaf]:
                bigest = leftLeaf
            if self.size >= rightLeaf and self.data[bigest] < self.data[rightLeaf]:
                bigest = rightLeaf

            if bigest != idx:
                self.data[idx], self.data[bigest] = self.data[bigest], self.data[idx]
                idx = bigest
            else:
                break

    def priorChk(self, target):
        parent = target // 2
        if self.data[parent] >= self.data[target]:
            return False
        self.data[parent], self.data[target] = self.data[target], self.data[parent]
        return True


class MinHeap(Heap):
    def heapify(self, idx):
        while idx <= self.size // 2:
            leftLeaf = idx * 2
            rightLeaf = idx * 2 + 1
            smalst = idx
            if self.size >= leftLeaf and self.data[smalst] > self.data[leftLeaf]:
                smalst = leftLeaf
            if self.size >= rightLeaf and self.data[smalst] > self.data[rightLeaf]:
                smalst = rightLeaf

            if smalst != idx:
                self.data[idx], self.data[smalst] = self.data[smalst], self.data[idx]
                idx = smalst
            else:
                break

    def priorChk(self, target):
        parent = target // 2
        if self.data[parent] <= self.data[target]:
            return False
        self.data[parent], self.data[target] = self.data[target], self.data[parent]
        return True


def solve():
    input = sys.stdin.readline
    N = int(input())
    overMid = MinHeap()
    underMid = MaxHeap()
    TC = []
    for _ in range(N):
        TC.append(int(input()))
    for t in TC:
        if underMid.size == 0:
            underMid.push(t)
        elif overMid.size >= underMid.size:
            if t <= overMid.top():
                underMid.push(t)
            else:
                underMid.push(overMid.replace_top(t))
        else:
            if underMid.top() < t:
                overMid.push(t)
            else:
                overMid.push(underMid.replace_top(t))
        print(underMid.top())

    return


if __name__ == "__main__":
    solve()
