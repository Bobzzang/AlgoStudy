# https://www.acmicpc.net/problem/20153


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    DefNum = 0
    for n in Nums:
        DefNum ^= n
    MaxNum = DefNum
    for n in Nums:
        TempNum = DefNum ^ n
        if TempNum > MaxNum:
            MaxNum = TempNum
    print(MaxNum, end="")
    print(MaxNum)
    return


if __name__ == "__main__":
    solve()
