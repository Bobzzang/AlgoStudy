# https://www.acmicpc.net/problem/1198

import sys


def Calc_Area(P1, P2, P3):
    # P[0] : x
    # P[1] : y
    S = (
        abs(
            (P1[0] * P2[1] + P2[0] * P3[1] + P3[0] * P1[1])
            - (P1[1] * P2[0] + P2[1] * P3[0] + P3[1] * P1[0])
        )
        / 2
    )
    return S


def solve():
    input = sys.stdin.readline
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    MaxS = 0
    for i in range(len(P)):
        for j in range(i, len(P)):
            for k in range(j, len(P)):
                S = Calc_Area(P[i], P[j], P[k])
                if S > MaxS:
                    MaxS = S
    print(MaxS)


if __name__ == "__main__":
    solve()
