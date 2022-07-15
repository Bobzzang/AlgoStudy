# https://www.acmicpc.net/problem/14426

import sys


def cnt_prefix(TarStr, RefSet):
    for s in RefSet:
        IsPrefix = True
        if len(s) < len(TarStr):
            continue
        for i, c in enumerate(TarStr):
            if s[i] != c:
                IsPrefix = False
                break
        if IsPrefix:
            return 1
    return 0


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    RefSet = []
    for _ in range(N):
        RefSet.append(input().rstrip())

    Prefix = []
    for _ in range(M):
        Prefix.append(input().rstrip())

    res = 0
    for Ref in Prefix:
        res += cnt_prefix(Ref, RefSet)

    print(res)
    return


if __name__ == "__main__":
    solve()
