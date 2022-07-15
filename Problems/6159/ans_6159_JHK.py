# https://www.acmicpc.net/problem/6159

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
    N, S = map(int, input().split())
    Cow = [int(input()) for _ in range(N)]
    Cow = merge_sort(Cow)
    cnt = 0
    j = len(Cow) - 1
    i = j - 1
    while j > 0:
        if Cow[j] > S:
            j -= 1
            i = j - 1
            continue
        val = Cow[i] + Cow[j]
        if val > S:
            if i == 0:
                j -= 1
                i = j - 1
            else:
                i -= 1
            continue
        if val <= S:
            cnt += i + 1
            j -= 1
            i = j - 1
            continue
    print(cnt)
    return


if __name__ == "__main__":
    solve()
