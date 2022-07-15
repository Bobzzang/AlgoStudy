# https://www.acmicpc.net/problem/6236

import sys


def check_usage_limit(limit, Usage):
    res = 0
    remain = 0
    for u in Usage:
        if u > remain:
            remain = limit
            res += 1
        if u > remain:
            # 제한금액으로 살 수 없는 경우
            return -1
        remain -= u
    return res


def bs(Target, Usage):
    left = 0
    right = max(Usage) * len(Usage)
    while left < right:
        mid = (left + right) // 2
        ref = check_usage_limit(mid, Usage)
        if ref == -1:
            left = mid + 1
        elif ref > Target:
            left = mid + 1
        else:
            right = mid
    mid = (left + right) // 2
    return mid


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Usage = []
    for _ in range(N):
        Usage.append(int(input()))
    print(bs(M, Usage))
    return


if __name__ == "__main__":
    solve()
