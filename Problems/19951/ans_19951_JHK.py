# https://www.acmicpc.net/problem/19951

import enum
import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    OrgCmd = [list(map(int, input().split())) for _ in range(M)]
    FixCmd = [0] * (N + 1)
    for cmd in OrgCmd:
        FixCmd[cmd[0] - 1] += cmd[2]
        FixCmd[cmd[1]] -= cmd[2]
    PSum = 0
    for i, v in enumerate(H):
        PSum += FixCmd[i]
        H[i] += PSum
    print(*H)
    return


if __name__ == "__main__":
    solve()
