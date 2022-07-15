# https://www.acmicpc.net/problem/14627

import sys


def count_chicken(Onion, Tar):
    cnt = 0
    for one in Onion:
        cnt += one // Tar
    return cnt


def search_max_onion(Onion, C):
    left = 1
    right = 1000000001
    while right - left > 1:
        mid = (left + right) // 2
        cnt = count_chicken(Onion, mid)
        if cnt >= C:
            left = mid
        else:
            right = mid
    return left


def solve():
    input = sys.stdin.readline
    S, C = map(int, input().split())
    Onion = []
    for _ in range(S):
        Onion.append(int(input()))
    print(sum(Onion) - C * search_max_onion(Onion, C))
    return


if __name__ == "__main__":
    solve()
