# https://www.acmicpc.net/problem/2022


def check_valid(X, Y, C, D):
    Xh = (X ** 2 - D ** 2) ** 0.5
    # Xh : x 장대가 기대고 있는 건물 높이

    Yh = (Y ** 2 - D ** 2) ** 0.5
    # Yh : y 장대가 기대고 있는 건물 높이

    Dx = C * D / Xh
    # 교차점까지, x 장대 끝에서부터의 바닥 거리

    Dy = C * D / Yh
    # 교차점까지, y 장대 끝에서부터의 바닥 거리

    # 10-3 절대/상대오차 범위 적용
    if Dx + Dy > (D * 1000 + 1) // 1 / 1000:
        return 1
    elif Dx + Dy < (D * 1000) // 1 / 1000:
        return -1
    else:
        return 0


def bs(X, Y, C):
    left = 0
    right = min(X, Y)
    while left < right:
        D = (left + right) / 2
        # D: 건물 사이 거리
        res = check_valid(X, Y, C, D)
        if res == 1:
            right = D
        elif res == -1:
            left = D
        else:
            return (D * 1000) // 1 / 1000


def solve():
    X, Y, C = map(float, input().split())
    print(bs(X, Y, C))


if __name__ == "__main__":
    solve()
