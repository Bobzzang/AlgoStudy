# https://www.acmicpc.net/problem/1166


def get_box_num(A, L, H, W):
    res = 1
    res *= L // A
    res *= H // A
    res *= W // A
    return res


def solve():
    N, L, H, W = map(int, input().split())
    left = 0
    right = min(L, H, W) + 1
    i = 0
    # while right-left < 10**-9:
    # 이렇게 할 경우 시간초과. right-left 가 소수계산 오차에 의해 좁혀지지 않는다는 듯.
    while i < 100:
        mid = (left + right) / 2
        if get_box_num(mid, L, H, W) >= N:
            left = mid
        else:
            right = mid
        i += 1
    print(left)
    return


if __name__ == "__main__":
    solve()
