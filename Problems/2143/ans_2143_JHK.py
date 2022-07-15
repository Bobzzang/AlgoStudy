# https://www.acmicpc.net/problem/2143

import sys


def cnt_partial_sum(Arr):
    end_sum_list = []
    tempSum = 0
    for v in Arr:
        tempSum += v
        end_sum_list.append(tempSum)
        # 0~i 까지의 합

    sum_list = []
    for i in range(len(end_sum_list)):
        sum_list.append(end_sum_list[i])
        for j in range(i):
            sum_list.append(end_sum_list[i] - end_sum_list[j])
            # Partial sum 모든 경우의 수를 list에 추가

    res = {}
    # 동일한 partial sum 결과에 대해 count
    for v in sum_list:
        if v not in res:
            res[v] = 1
        else:
            res[v] += 1
    return res


def solve():
    input = sys.stdin.readline
    T = int(input())
    N = int(input())
    NArr = list(map(int, input().split()))
    M = int(input())
    MArr = list(map(int, input().split()))
    NCnt = cnt_partial_sum(NArr)
    MCnt = cnt_partial_sum(MArr)
    ans = 0
    for val, cnt in NCnt.items():
        TarVal = T - val
        if TarVal in MCnt:
            ans += MCnt[TarVal] * cnt

    print(ans)
    return


if __name__ == "__main__":
    solve()
