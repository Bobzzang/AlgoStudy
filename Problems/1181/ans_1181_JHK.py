# https://www.acmicpc.net/problem/1181

# 풀어놓고 나니 class 사용한 장점이 없다

import sys


class StrList:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def sort(self):
        return self.mergeSort(self.list)

    def mergeSort(self, data):
        if len(data) < 2:
            return data
        mid = (len(data)) // 2
        left = []
        right = []
        for i, v in enumerate(data):
            if i != mid:
                compResult = self.compare(data[mid], data[i])
                if compResult == True:
                    left.append(data[i])
                elif compResult == False:
                    right.append(data[i])

        return self.mergeSort(left) + [data[mid]] + self.mergeSort(right)

    def compare(self, ref, tar):
        if len(ref) > len(tar):
            return True
        elif len(ref) < len(tar):
            return False
        else:
            for i in range(len(ref)):
                if ref[i] > tar[i]:
                    return True
                elif ref[i] < tar[i]:
                    return False
            return  # None

    def size(self):
        return len(self.list)


def solve():
    input = sys.stdin.readline
    N = int(input())
    strList = StrList()
    for _ in range(N):
        strList.push(str(input().rstrip()))
    ret = strList.sort()
    for r in ret:
        print(r)
    return


if __name__ == "__main__":
    solve()
