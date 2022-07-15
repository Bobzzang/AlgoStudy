# https://www.acmicpc.net/problem/11578

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Students = []
    for _ in range(M):
        tempStd = list(map(int, input().split()))
        Students.append(tempStd[1:])

    binLength = len(bin((2 ** M) - 1)[2:])
    MinStd = M + 1
    for sel in range(1, 2 ** M):
        binSel = f"{sel:0{binLength}b}"
        res = 0
        for idx, val in enumerate(binSel):
            if val == "1":
                for p in Students[idx]:
                    res |= 1 << (p - 1)
        if 2 ** N == res + 1:
            if binSel.count("1") < MinStd:
                MinStd = binSel.count("1")
    if MinStd == M + 1:
        print(-1)
        return
    print(MinStd)
    return


if __name__ == "__main__":
    solve()
