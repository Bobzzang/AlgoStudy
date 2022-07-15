# https://www.acmicpc.net/problem/17390

import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))


def solve():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    TC = [tuple(map(int, input().split())) for _ in range(Q)]
    SortedA = merge_sort(A)
    PSum = [0]
    tempSum = 0
    for n in SortedA:
        tempSum += n
        PSum.append(tempSum)
    for T in TC:
        s, e = T
        print(PSum[e] - PSum[s - 1])
    return


if __name__ == "__main__":
    solve()
