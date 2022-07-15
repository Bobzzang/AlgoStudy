# https://www.acmicpc.net/problem/12865

import sys


def solve():
    input = sys.stdin.readline
    N, MaxWeight = map(int, input().split())
    stuffs = [tuple(map(int, input().split())) for _ in range(N)]
    # stuffs = (weight, value)
    dp = [0] * (MaxWeight + 1)
    for i, stuff in enumerate(stuffs):
        for j in range(MaxWeight, 0, -1):
            if j >= stuff[0]:
                dp[j] = max(dp[j], dp[j - stuff[0]] + stuff[1])
                # j 무게가 남았을 때, i번째 물건을 넣지 않을 경우(기존 최댓값) vs 넣을 경우
    print(dp[MaxWeight])
    return


if __name__ == "__main__":
    solve()
