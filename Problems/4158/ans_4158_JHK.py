# https://www.acmicpc.net/problem/4158

import sys


def solve():
    input = sys.stdin.readline
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            return
        SG = [int(input()) for _ in range(N)]
        SY = [int(input()) for _ in range(M)]
        i = 0
        j = 0
        cnt = 0
        while i < N and j < M:
            if SG[i] == SY[j]:
                cnt += 1
                i += 1
                j += 1
            elif SG[i] > SY[j]:
                j += 1
            else:
                i += 1
        print(cnt)
    return


if __name__ == "__main__":
    solve()
