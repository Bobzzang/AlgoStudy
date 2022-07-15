# https://www.acmicpc.net/problem/11561

import sys


def print_num(N):
    if N == 1:
        print(1)
        return
    left = 0
    right = N
    # right limit을 줄여두고 싶지만 적절한 식이 생각이 안남.
    while right - left > 1:
        mid = (left + right) // 2
        SeriesSum = mid * (mid + 1) // 2
        if SeriesSum == N:
            print(mid)
            return
        if SeriesSum > N:
            right = mid
        else:
            left = mid
    print(left)
    return


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = [int(input()) for _ in range(T)]
    for N in TC:
        print_num(N)
    return


if __name__ == "__main__":
    solve()
