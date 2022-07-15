# https://www.acmicpc.net/problem/1358

import sys


def check_rect(x, y, W, H, X0, Y0):
    if x < X0:
        return False
    if y < Y0:
        return False
    if x > X0 + W:
        return False
    if y > Y0 + H:
        return False
    return True


def check_LeftCircle(x, y, W, H, X0, Y0):
    r = H / 2
    p = X0
    q = Y0 + r
    if x > p:
        return False
    if (x - p) ** 2 + (y - q) ** 2 > r ** 2:
        return False
    return True


def check_RightCircle(x, y, W, H, X0, Y0):
    r = H / 2
    p = X0 + W
    q = Y0 + r
    if x < p:
        return False
    if (x - p) ** 2 + (y - q) ** 2 > r ** 2:
        return False
    return True


def check_inside(x, y, W, H, X0, Y0):
    if check_rect(x, y, W, H, X0, Y0):
        return 1
    if check_LeftCircle(x, y, W, H, X0, Y0):
        return 1
    if check_RightCircle(x, y, W, H, X0, Y0):
        return 1
    return 0


def solve():
    input = sys.stdin.readline
    W, H, X, Y, P = map(int, input().split())
    Person = []
    for _ in range(P):
        tempX, tempY = map(int, input().split())
        Person.append((tempX, tempY))
    cnt = 0
    for per in Person:
        cnt += check_inside(*per, W, H, X, Y)

    print(cnt)
    return


if __name__ == "__main__":
    solve()
