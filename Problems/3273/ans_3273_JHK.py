# https://www.acmicpc.net/problem/3273

import sys


def merge(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1

    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    left = mergeSort(arr[: len(arr) // 2])
    right = mergeSort(arr[len(arr) // 2 :])
    return merge(left, right)


def bs(X, nums, i, j):
    tar = X - nums[i]
    i += 1
    # i 시작값은 탐색 할 필요 없음.
    while i < j:
        mid = (i + j) // 2
        if nums[mid] > tar:
            j = mid - 1
        elif nums[mid] < tar:
            i = mid + 1
        else:
            return mid

    mid = (i + j) // 2
    return mid


def solve():
    input = sys.stdin.readline
    N = int(input())
    tempNums = list(map(int, input().split()))
    X = int(input())
    nums = mergeSort(tempNums)
    res = 0
    i = 0
    j = len(nums) - 1
    while i < j:
        j = bs(X, nums, i, j)
        if nums[i] + nums[j] == X:
            res += 1
        i += 1
    print(res)
    return


if __name__ == "__main__":
    solve()
