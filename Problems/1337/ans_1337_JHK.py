# https://www.acmicpc.net/problem/1337

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
    N = int(input())
    Nums = [int(input()) for _ in range(N)]
    Nums = merge_sort(Nums)

    Min_Need = 5
    for i in range(len(Nums)):
        cnt = 0
        for j in range(i, min(i + 5, len(Nums))):
            if Nums[j] <= Nums[i] + 4:
                cnt += 1
        if Min_Need > 5 - cnt:
            Min_Need = 5 - cnt
    print(Min_Need)
    return


if __name__ == "__main__":
    solve()
