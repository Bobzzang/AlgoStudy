# https://www.acmicpc.net/problem/2751
# pypy3로 성공함. Python3로는 안된다하네...

import sys


def merge(s, e, m):
    i = s
    j = m + 1
    ret = []
    while i <= m and j <= e:
        if inData[i] < inData[j]:
            ret.append(inData[i])
            i += 1
        else:
            ret.append(inData[j])
            j += 1

    while i <= m:
        ret.append(inData[i])
        i += 1
    while j <= e:
        ret.append(inData[j])
        j += 1

    i = s
    j = 0
    while i <= e:
        inData[i] = ret[j]
        i += 1
        j += 1


def mergeSort(s, e):
    if s < e:
        m = (s + e) // 2
        mergeSort(s, m)
        mergeSort(m + 1, e)
        merge(s, e, m)


def solve():
    input = sys.stdin.readline
    global inData
    N = int(input())
    inData = []
    for _ in range(N):
        inData.append(int(input()))
    mergeSort(0, len(inData) - 1)

    print(*inData)


if __name__ == "__main__":
    solve()
