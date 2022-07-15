# https://www.acmicpc.net/problem/2725

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = [int(input()) for _ in range(N)]
    CntList = [0, 3]
    for i in range(2, max(TC) + 1):
        cnt = 0
        for j in range(1, i):
            p, q = i, j
            while q != 0:
                p, q = q, p % q
            if p == 1:
                cnt += 1
        CntList.append(cnt * 2)
    PSum = []
    TempPSum = 0
    for cnt in CntList:
        TempPSum += cnt
        PSum.append(TempPSum)
    for t in TC:
        print(PSum[t])
    return


if __name__ == "__main__":
    solve()
