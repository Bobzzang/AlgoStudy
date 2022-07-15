# https://www.acmicpc.net/problem/4779

import sys


def get_cantor(orgStr):
    blankStr = " " * len(orgStr)
    resStr = orgStr + blankStr + orgStr
    return resStr


def solve():
    Lines = sys.stdin.readlines()
    for N in Lines:
        N = int(N.rstrip())
        S = "-"
        for _ in range(N):
            S = get_cantor(S)
        print(S)
    return


if __name__ == "__main__":
    solve()
