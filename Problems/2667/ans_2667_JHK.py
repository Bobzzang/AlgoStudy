# https://www.acmicpc.net/problem/2667

import sys


def searchAround(N, Houses, res, i, j):
    res[-1] += 1
    Houses[i][j] = 0
    if i > 0:
        if Houses[i - 1][j] == 1:
            searchAround(N, Houses, res, i - 1, j)
    if i < N - 1:
        if Houses[i + 1][j] == 1:
            searchAround(N, Houses, res, i + 1, j)
    if j > 0:
        if Houses[i][j - 1] == 1:
            searchAround(N, Houses, res, i, j - 1)
    if j < N - 1:
        if Houses[i][j + 1] == 1:
            searchAround(N, Houses, res, i, j + 1)

    return


def solve():
    input = sys.stdin.readline
    N = int(input())
    Houses = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    res = []
    for i in range(N):
        for j in range(N):
            if Houses[i][j] != 0:
                res.append(0)
                searchAround(N, Houses, res, i, j)

    res.sort()
    print(len(res))
    print(*res)
    return


if __name__ == "__main__":
    solve()
