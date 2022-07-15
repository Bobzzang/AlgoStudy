# https://www.acmicpc.net/problem/17427


def solve():
    N = int(input())
    res = 0
    for i in range(1, N + 1):
        res += N - (N % i)
    print(res)
    return


if __name__ == "__main__":
    solve()
