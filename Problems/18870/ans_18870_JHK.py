# https://www.acmicpc.net/problem/18870

import sys


def merge(left, right):
    leftIdx = 0
    rightIdx = 0
    ret = []
    while len(left) > leftIdx and len(right) > rightIdx:
        if left[leftIdx] < right[rightIdx]:
            ret.append(left[leftIdx])
            leftIdx += 1
        else:
            ret.append(right[rightIdx])
            rightIdx += 1

    while len(left) > leftIdx:
        ret.append(left[leftIdx])
        leftIdx += 1
    while len(right) > rightIdx:
        ret.append(right[rightIdx])
        rightIdx += 1

    return ret


def mergeSort(data):
    if len(data) < 2:
        return data
    return merge(mergeSort(data[: len(data) // 2]), mergeSort(data[len(data) // 2 :]))


def solve():
    input = sys.stdin.readline
    N = int(input())
    InData = list(map(int, input().split()))
    ret = mergeSort(InData)

    beforeVal = None
    idx = 0
    dic = {}
    for r in ret:
        if r not in dic:
            dic[r] = idx
            idx += 1

    for i in InData[:-1]:
        print(dic[i], end=" ")
    print(dic[InData[-1]])
    return


if __name__ == "__main__":
    solve()
