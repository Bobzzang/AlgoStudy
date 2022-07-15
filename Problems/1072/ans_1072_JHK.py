# https://www.acmicpc.net/problem/1072

# Binary search 문제로 분류가 되는데 그냥 수학으로 해결이 되버렸기에,
# Binary search로 다시 품.


def solve():
    X, Y = map(int, input().split())
    # Z = Y * 100 // X
    LoseGame = X - Y
    LoseRate = LoseGame * 100 // X
    LoseRateRes = LoseGame * 100 % X
    if LoseRateRes == 0:
        if LoseRate == 1:
            print(-1)
            return
        NewLoseRate = LoseRate - 1
        if LoseGame * 100 % NewLoseRate > 0:
            res = LoseGame * 100 // NewLoseRate + 1 - X
        else:
            res = LoseGame * 100 // NewLoseRate - X
    else:
        if LoseRate == 0:
            print(-1)
            return
        NewLoseRate = LoseRate
        if LoseGame * 100 % NewLoseRate > 0:
            res = LoseGame * 100 // NewLoseRate + 1 - X
        else:
            res = LoseGame * 100 // NewLoseRate - X
    if res < 0:
        print(-1)
    else:
        print(res)

    return


if __name__ == "__main__":
    solve()
