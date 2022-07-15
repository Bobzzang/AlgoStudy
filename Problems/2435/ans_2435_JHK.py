# https://www.acmicpc.net/problem/2435


def solve():
    N, K = map(int, input().split())
    Temperature = list(map(int, input().split()))
    i = 0
    DaySum = 0
    while i < K:
        DaySum += Temperature[i]
        i += 1
    MaxTemp = DaySum
    i = K
    while i < len(Temperature):
        DaySum += Temperature[i] - Temperature[i - K]
        i += 1
        if DaySum > MaxTemp:
            MaxTemp = DaySum
    print(MaxTemp)
    return


if __name__ == "__main__":
    solve()
