# https://www.acmicpc.net/problem/14445


def solve():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        print(N // 2)
        return
    print(N // 2 + 1)
    return


if __name__ == "__main__":
    solve()
