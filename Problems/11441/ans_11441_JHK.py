# https://www.acmicpc.net/problem/11441

import sys


def solve():

    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    TN = int(input())
    TS = [list(map(int, input().split())) for _ in range(TN)]
    PSum = [0]
    for x in arr:
        PSum.append(PSum[-1] + x)
    for p, q in TS:
        print(PSum[q] - PSum[p - 1])
    return


if __name__ == "__main__":
    solve()
