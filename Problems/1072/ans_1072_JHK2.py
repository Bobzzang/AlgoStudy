# https://www.acmicpc.net/problem/1072


def bs(X, Y, target):
    # Target이 되는 최솟값 찾기
    left = 0
    right = X
    while left < right:
        mid = (left + right) // 2
        WinRate = (Y + mid) * 100 // (X + mid)
        if WinRate >= target:
            right = mid
        else:
            left = mid + 1
    print(left)
    return


def solve():
    X, Y = map(int, input().split())
    WinRate = Y * 100 // X
    if WinRate >= 99:
        # 더이상 승률이 상승 할 수 없음.
        print(-1)
        return
    bs(X, Y, WinRate + 1)
    return


if __name__ == "__main__":
    solve()
