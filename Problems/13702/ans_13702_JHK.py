# https://www.acmicpc.net/problem/13702

import sys


def can_distribute(Mak: list, K, Target):
    cnt = 0
    for m in Mak:
        cnt += m // Target
    return cnt >= K


def BS(Mak, K):
    left = 0
    right = max(Mak) + 1
    while left + 1 < right:
        mid = (left + right) // 2
        res = can_distribute(Mak, K, mid)
        if res:
            left = mid
        else:
            right = mid
    return left


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    Mak = []
    for _ in range(N):
        Mak.append(int(input()))
    print(BS(Mak, K))
    return


if __name__ == "__main__":
    solve()
