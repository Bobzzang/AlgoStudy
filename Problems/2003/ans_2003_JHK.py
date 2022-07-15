# https://www.acmicpc.net/problem/2003


def solve():
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))
    left = 0
    right = 0
    PSum = Data[0]
    cnt = 0
    while True:
        if PSum == M:
            cnt += 1
            right += 1
            if right >= len(Data):
                break
            PSum += Data[right] - Data[left]
            left += 1
        elif PSum > M:
            PSum -= Data[left]
            left += 1
        else:
            right += 1
            if right >= len(Data):
                break
            PSum += Data[right]
    print(cnt)
    return


if __name__ == "__main__":
    solve()
