# https://www.acmicpc.net/problem/2294

import sys


def get_min_coin(Target, Coin_cnt_dic):
    if Target == 0:
        return 10001
    if Coin_cnt_dic[Target] != 0:
        return Coin_cnt_dic[Target]
    min_coin = 10001
    i = 1
    while i <= Target // 2:
        cnt_coin = get_min_coin(i, Coin_cnt_dic) + get_min_coin(
            Target - i, Coin_cnt_dic
        )
        if min_coin > cnt_coin:
            min_coin = cnt_coin
        i += 1
    Coin_cnt_dic[Target] = min_coin
    return min_coin


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    coin = [int(input()) for _ in range(N)]
    Coin_cnt_dic = [0] * (K + 1)
    for c in coin:
        if c < len(Coin_cnt_dic):
            Coin_cnt_dic[c] = 1
    for i in range(1, K + 1):
        get_min_coin(i, Coin_cnt_dic)
        # recursion 제한 회피 (k >1000 이므로 재귀 제한에 걸림.)
    res = get_min_coin(K, Coin_cnt_dic)
    if res >= 10001:
        print(-1)
    else:
        print(res)
    return


if __name__ == "__main__":
    solve()
