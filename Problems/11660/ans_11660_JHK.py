# https://www.acmicpc.net/problem/11660

import sys


def get_area_sum(N, x1, y1, x2, y2, PSumTable):
    res = 0
    for x in range(x1, x2 + 1):
        if y1 == 0:
            res += PSumTable[x * N + y2]
        else:
            res += PSumTable[x * N + y2] - PSumTable[x * N + y1 - 1]
    return res


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Table = []
    for _ in range(N):
        Table += list(map(int, input().split()))
    TC = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        TC.append((x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    PSumTable = []
    for i in range(N):
        TempSum = 0
        for j in range(N):
            TempSum += Table[i * N + j]
            PSumTable.append(TempSum)
    for pos in TC:
        print(get_area_sum(N, *pos, PSumTable))
    return


if __name__ == "__main__":
    solve()
