# https://www.acmicpc.net/problem/11651

import sys


def sortPriorY(data):
    if len(data) > 1:
        left = []
        right = []
        mid = data[0]
        for i in range(1, len(data)):
            if mid[1] > data[i][1]:
                right.append(data[i])
            elif mid[1] < data[i][1]:
                left.append(data[i])
            else:
                if mid[0] > data[i][0]:
                    right.append(data[i])
                else:
                    left.append(data[i])
        return sortPriorY(right) + [mid] + sortPriorY(left)
    else:
        return data


def solve():
    input = sys.stdin.readline
    N = int(input())
    inpData = []
    for _ in range(N):
        inpData.append(tuple(map(int, input().split())))

    res = sortPriorY(inpData)
    for r in res:
        print(*r)

    return


if __name__ == "__main__":
    solve()
