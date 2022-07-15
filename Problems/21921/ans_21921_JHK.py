# https://www.acmicpc.net/problem/21921


def solve():
    N, X = map(int, input().split())
    Visit = list(map(int, input().split()))
    PSum = sum(Visit[:X])
    MaxX = PSum
    i = 0
    cnt = 1
    while X + i < len(Visit):
        PSum -= Visit[i]
        PSum += Visit[X + i]
        if MaxX == PSum:
            cnt += 1

        elif MaxX < PSum:
            MaxX = PSum
            cnt = 1

        i += 1
    if MaxX == 0:
        print("SAD")
    else:
        print(MaxX)
        print(cnt)
    return


if __name__ == "__main__":
    solve()
