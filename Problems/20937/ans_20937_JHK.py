# https://www.acmicpc.net/problem/20937


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    Cnt = [0] * 50001
    for num in Nums:
        Cnt[num] += 1
    print(max(Cnt))
    return


if __name__ == "__main__":
    solve()
