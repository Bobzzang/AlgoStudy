# https://www.acmicpc.net/problem/12968


def solve():
    R, C, K = map(int, input().split())
    if K == 1:
        print(1)
        return
    Num = R * C
    if Num % 2 == 0:
        print(1)
    else:
        print(0)
    return


if __name__ == "__main__":
    solve()
