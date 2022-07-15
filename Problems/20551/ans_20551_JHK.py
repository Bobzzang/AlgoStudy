# https://www.acmicpc.net/problem/20551

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


def bs(Nums, Target):
    left = 0
    right = len(Nums) - 1
    mid = (left + right) // 2
    while right - left > 0:
        if Target > Nums[mid]:
            left = mid + 1
        else:
            right = mid
        mid = (left + right) // 2
    if Nums[mid] != Target:
        return -1
    return mid


def solve():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    Questions = [int(input()) for _ in range(M)]
    Nums = merge_sort(A)
    for q in Questions:
        print(bs(Nums, q))
    return


if __name__ == "__main__":
    solve()
