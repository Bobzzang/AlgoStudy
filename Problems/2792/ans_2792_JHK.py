# https://www.acmicpc.net/problem/2792

import sys


def check_sep(N, Target, Reflist):
    res = 0
    for val in Reflist:
        if val % Target > 0:
            res += 1
        res += val // Target
    if res <= N:
        return True
    return False


def bs(N, Reflist):
    left = 0
    right = max(Reflist)
    while left < right:
        mid = (left + right) // 2
        if mid == 0:
            break
        if check_sep(N, mid, Reflist):
            right = mid
        else:
            left = mid + 1
    return right


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Gems = []
    for _ in range(M):
        Gems.append(int(input()))

    print(bs(N, Gems))
    return


if __name__ == "__main__":
    solve()
