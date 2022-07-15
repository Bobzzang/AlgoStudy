# https://www.acmicpc.net/problem/10025

import sys


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    Ice = [0] * 1000001
    for _ in range(N):
        g, x = map(int, input().split())
        Ice[x] = g
    PSum = sum(Ice[: 2 * K + 1])
    PSumMax = PSum
    i = 1
    while 2 * K + i < len(Ice):
        PSum -= Ice[i - 1]
        PSum += Ice[2 * K + i]
        if PSum > PSumMax:
            PSumMax = PSum
        i += 1
    print(PSumMax)
    return


if __name__ == "__main__":
    solve()
