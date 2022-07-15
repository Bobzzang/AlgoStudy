# https://www.acmicpc.net/problem/11811

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    A = []
    for i in range(N):
        res = 0
        for j in range(N):
            res |= mat[i][j]
        A.append(res)
    print(*A)
    return


if __name__ == "__main__":
    solve()
