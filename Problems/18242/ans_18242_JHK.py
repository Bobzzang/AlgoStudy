# https://www.acmicpc.net/problem/18242


def solve():
    N, M = map(int, input().split())
    Base = [input() for _ in range(N)]
    i = 0
    while True:
        FillCount = Base[i].count("#")
        if FillCount != 0:
            if FillCount % 2 == 0:
                print("UP")
                return
            else:
                FillStart = Base[i].find("#")
                FillEnd = FillStart + FillCount - 1
                break
        i += 1
    StartRow = i
    # Check Left
    cnt = 0
    while i < N:
        if Base[i][FillStart] == "#":
            cnt += 1
        else:
            break
        i += 1
    if cnt != FillCount:
        print("LEFT")
        return

    # Check Right
    i = StartRow
    cnt = 0
    while i < N:
        if Base[i][FillEnd] == "#":
            cnt += 1
        else:
            break
        i += 1
    if cnt != FillCount:
        print("RIGHT")
        return
    print("DOWN")
    return


if __name__ == "__main__":
    solve()
