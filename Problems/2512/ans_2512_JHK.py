# https://www.acmicpc.net/problem/2512

import sys


def sumBudget(ReqList, Limit):
    res = 0
    for req in ReqList:
        if req > Limit:
            res += Limit
        else:
            res += req
    return res


def bs(ReqList, Target):
    left = 0
    right = Target + 1
    while right - left > 1:
        mid = (left + right) // 2
        tempSum = sumBudget(ReqList, mid)
        if tempSum > Target:
            right = mid
        else:
            left = mid

    return left


def solve():
    input = sys.stdin.readline
    N = int(input())
    BudgetReq = list(map(int, input().split()))
    Budget = int(input())
    if sum(BudgetReq) <= Budget:
        print(max(BudgetReq))
        return
    print(bs(BudgetReq, Budget))
    return


if __name__ == "__main__":
    solve()
