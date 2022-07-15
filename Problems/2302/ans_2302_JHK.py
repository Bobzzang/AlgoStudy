# https://www.acmicpc.net/problem/2302

import sys


def get_method(Num, memo):
    if memo[Num] != 0:
        return memo[Num]
    memo[Num] = get_method(Num - 2, memo) * 2 + get_method(Num - 3, memo)
    return memo[Num]


def solve():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    if N == 1:
        print(1)
        return
    Fixed = [0] + [int(input()) for _ in range(M)] + [N + 1]
    memo = [0] * (N + 1)
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2

    cnt = 1
    for i in range(len(Fixed) - 1):
        Num_Between = Fixed[i + 1] - Fixed[i] - 1
        cnt *= get_method(Num_Between, memo)
    print(cnt)
    return


if __name__ == "__main__":
    solve()
