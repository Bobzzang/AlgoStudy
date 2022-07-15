# https://www.acmicpc.net/problem/17298

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    InData = list(map(int, input().split()))
    RB_Stack = []
    res = [-1]
    for i in range(len(InData) - 2, -1, -1):
        if InData[i] < InData[i + 1]:
            RB_Stack.append(InData[i + 1])
            res.append(InData[i + 1])
        else:
            while True:
                if len(RB_Stack) == 0:
                    res.append(-1)
                    break
                elif InData[i] < RB_Stack[-1]:
                    res.append(RB_Stack[-1])
                    break
                else:
                    RB_Stack.pop()

    print(*list(reversed(res)))
    return


if __name__ == "__main__":
    solve()
