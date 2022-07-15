# https://www.acmicpc.net/problem/11052


def max_price(P, TotPrice, Target):
    if Target == 0:
        return 0
    if TotPrice[Target] != 0:
        return TotPrice[Target]
    if Target < len(P):
        MaxPrice = P[Target]
    else:
        MaxPrice = 0
    i = 1
    while i < Target:
        TempPrice = max_price(P, TotPrice, i) + max_price(P, TotPrice, Target - i)
        if MaxPrice < TempPrice:
            MaxPrice = TempPrice
        i += 1
    TotPrice[Target] = MaxPrice
    return TotPrice[Target]


def solve():
    N = int(input())
    P = [0] + list(map(int, input().split()))
    TotPrice = [0] * len(P)
    # for i in range(1, N + 1):
    #     max_price(P, TotPrice, i)
    # 안해도 재귀 호출 error 발생 안함.
    print(max_price(P, TotPrice, N))
    return


def Fail_greedy():
    N = int(input())
    P = [0] + list(map(int, input().split()))
    Eff = [0] * len(P)
    for i, v in enumerate(P):
        if i != 0:
            Eff[i] = v / i
    PriceSum = 0
    MaxEffIdx = Eff.index(max(Eff))
    while N > 0:
        if MaxEffIdx <= N:
            PriceSum += P[MaxEffIdx]
            N -= MaxEffIdx
        else:
            MaxEffIdx = Eff.index(max(Eff[:MaxEffIdx]))
    print(PriceSum)
    return


if __name__ == "__main__":
    solve()
