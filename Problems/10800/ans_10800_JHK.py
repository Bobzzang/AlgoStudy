# https://www.acmicpc.net/problem/10800

import sys


def merge_sp(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i][2] == right[j][2]:
            if left[i][1] < right[j][1]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        elif left[i][2] < right[j][2]:
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


def merge_sort_sp(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort_sp(arr[: len(arr) // 2])
    right = merge_sort_sp(arr[len(arr) // 2 :])
    return merge_sp(left, right)


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = []

    for i in range(N):
        Ball, Size = map(int, input().split())
        Ball -= 1
        TC.append((i, Ball, Size))
    TotalBalls = merge_sort_sp(TC)
    # TotalBalls : Size -> Color 순으로 정렬된 공

    TotSum = 0
    ColorSum = [0] * N
    Res = [0] * N
    i = 0
    j = 0
    for i in range(len(TotalBalls)):
        while TotalBalls[i][2] > TotalBalls[j][2]:
            TotSum += TotalBalls[j][2]
            ColorSum[TotalBalls[j][1]] += TotalBalls[j][2]
            j += 1
        Res[TotalBalls[i][0]] = TotSum - ColorSum[TotalBalls[i][1]]
    for r in Res:
        print(r)
    return


if __name__ == "__main__":
    solve()
