# https://www.acmicpc.net/problem/7579

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    memoryCost = list(map(int, input().split()))
    gain = list(map(int, input().split()))
    Apps = list(zip(memoryCost, gain))
    TotalCost = sum(memoryCost)
    TotalGain = sum(gain)
    TargetCost = TotalCost - M
    # TargetCost 이하로 Running 중으로 "남길"  App을 선택, 이 때 기대 gain을 최대가 되도록 선택
    # --> 기본적인 Knapsack 문제와 같아짐.
    dp = [0] * (TargetCost + 1)
    # dp[i] : i 비용 이하로 Running 중인 App의 기대 gain 최대합
    for app in Apps:
        for i in range(TargetCost, -1, -1):
            if i >= app[0]:
                dp[i] = max(dp[i], dp[i - app[0]] + app[1])
                # 해당 App을 선택하지 않았을 때 vs 선택하였을 때

    print(TotalGain - dp[TargetCost])
    return


if __name__ == "__main__":
    solve()
