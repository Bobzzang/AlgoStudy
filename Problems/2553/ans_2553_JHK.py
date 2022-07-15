# https://www.acmicpc.net/problem/2553


def solve():
    N = int(input())
    res = 1
    for i in range(1, N + 1):
        while i % 5 == 0:
            i //= 5
            res //= 2
        res %= 100000
        # 5^5 = 15625 이므로 그 이상 남겨야 함.
        res *= i
    res %= 10
    print(res)
    return


if __name__ == "__main__":
    solve()
