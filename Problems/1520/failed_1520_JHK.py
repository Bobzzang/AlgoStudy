# https://www.acmicpc.net/problem/1520

# 시간초과 - 단순 재귀 (from 0,0)

import sys


def checkAvail(data, avail, rowi, colj):
    ref = data[rowi][colj]
    if rowi > 0:
        if ref > data[rowi - 1][colj]:
            avail[rowi - 1][colj] += 1
            checkAvail(data, avail, rowi - 1, colj)
    if rowi < N - 1:
        if ref > data[rowi + 1][colj]:
            avail[rowi + 1][colj] += 1
            checkAvail(data, avail, rowi + 1, colj)
    if colj > 0:
        if ref > data[rowi][colj - 1]:
            avail[rowi][colj - 1] += 1
            checkAvail(data, avail, rowi, colj - 1)
    if colj < M - 1:
        if ref > data[rowi][colj + 1]:
            avail[rowi][colj + 1] += 1
            checkAvail(data, avail, rowi, colj + 1)


def solve():
    global N, M
    input = sys.stdin.readline
    N, M = map(int, input().split())
    avail = [[0] * M for _ in range(N)]
    res = [[0] * M for _ in range(N)]
    data = []
    for _ in range(N):
        data.append(tuple(map(int, input().split())))
    avail[0][0] = 1
    checkAvail(data, avail, 0, 0)

    print(avail[-1][-1])
    return


if __name__ == "__main__":
    solve()
