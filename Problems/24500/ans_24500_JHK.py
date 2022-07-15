# https://www.acmicpc.net/problem/24500


def solve():
    N = int(input())
    B = bin(N)
    MaxIdx = len(B) - 3
    Base = (1 << (MaxIdx + 1)) - 1
    if Base - N == 0:
        print(1)
        print(N)
    else:
        print(2)
        print(Base - N)
        print(N)
    return


if __name__ == "__main__":
    solve()
