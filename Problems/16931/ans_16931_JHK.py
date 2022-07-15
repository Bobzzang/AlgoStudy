# https://www.acmicpc.net/problem/16931

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Cubes = []
    for _ in range(N):
        Cubes.append(list(map(int, input().split())))

    Area = 0
    Area += N * M * 2

    for i in range(N):
        BeforeVal = 0
        for j in range(M):
            if Cubes[i][j] > BeforeVal:
                Area += Cubes[i][j] - BeforeVal
            BeforeVal = Cubes[i][j]

        BeforeVal = 0
        for j in range(M - 1, -1, -1):
            if Cubes[i][j] > BeforeVal:
                Area += Cubes[i][j] - BeforeVal
            BeforeVal = Cubes[i][j]

    for j in range(M):
        BeforeVal = 0
        for i in range(N):
            if Cubes[i][j] > BeforeVal:
                Area += Cubes[i][j] - BeforeVal
            BeforeVal = Cubes[i][j]

        BeforeVal = 0
        for i in range(N - 1, -1, -1):
            if Cubes[i][j] > BeforeVal:
                Area += Cubes[i][j] - BeforeVal
            BeforeVal = Cubes[i][j]

    print(Area)
    return


if __name__ == "__main__":
    solve()
