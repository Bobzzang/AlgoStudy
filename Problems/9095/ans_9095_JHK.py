# https://www.acmicpc.net/problem/9095

import sys


def get_cnt_num(num, memo):
    if num == 0:
        return 0
    if memo[num] != 0:
        return memo[num]
    memo[num] = (
        get_cnt_num(num - 1, memo)
        + get_cnt_num(num - 2, memo)
        + get_cnt_num(num - 3, memo)
    )
    return memo[num]


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = [int(input()) for _ in range(N)]
    memo = [0] * (max(TC) + 1)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    for num in TC:
        print(get_cnt_num(num, memo))
    return


if __name__ == "__main__":
    solve()
