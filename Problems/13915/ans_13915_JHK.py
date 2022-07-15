# https://www.acmicpc.net/problem/13915

import sys


def solve():
    InputData = sys.stdin.readlines()
    i = 0
    while i < len(InputData):
        N = int(InputData[i].rstrip())
        Maturity = set()
        for _ in range(N):
            i += 1
            res = 0
            for c in InputData[i].rstrip():
                res |= 1 << (int(c) - 1)
            Maturity.add(res)
        i += 1
        print(len(Maturity))
    return


if __name__ == "__main__":
    solve()
