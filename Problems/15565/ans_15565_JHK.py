# https://www.acmicpc.net/problem/15565

import sys


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    Dolls = list(map(int, input().split()))
    RyanIdx = []
    for i, v in enumerate(Dolls):
        if v == 1:
            RyanIdx.append(i)

    MinRyan = N + 1
    i = 0
    while i + K - 1 < len(RyanIdx):
        if MinRyan == K:
            break
        if MinRyan > RyanIdx[i + K - 1] - RyanIdx[i] + 1:
            MinRyan = RyanIdx[i + K - 1] - RyanIdx[i] + 1
        i += 1
    if MinRyan == N + 1:
        print(-1)
    else:
        print(MinRyan)


if __name__ == "__main__":
    solve()
