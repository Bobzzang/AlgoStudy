# https://www.acmicpc.net/problem/17829


import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
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


def get_secondMax(a, b, c, d):
    return merge_sort([a, b, c, d])[1]


def Pulling(dat, N):
    if N == 1:
        return dat
    res = []
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            res.append(
                get_secondMax(
                    dat[i * N + j],
                    dat[i * N + j + 1],
                    dat[(i + 1) * N + j],
                    dat[(i + 1) * N + j + 1],
                )
            )
    return Pulling(res, N // 2)


def solve():
    input = sys.stdin.readline
    N = int(input())
    Mat = []
    for _ in range(N):
        Mat += list(map(int, input().split()))
    print(*Pulling(Mat, N))
    return


if __name__ == "__main__":
    solve()
