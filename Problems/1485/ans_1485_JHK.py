# https://www.acmicpc.net/problem/1485

import sys


def is_square(Points):
    x, y = Points[0]
    LengthRes = []
    for i in range(1, 4):
        p, q = Points[i]
        LengthRes.append([(x - p) ** 2 + (y - q) ** 2, i])
    LengthRes.sort()
    # 가장 긴 거리(대각 지점)이 마지막에 위치
    if LengthRes[0][0] != LengthRes[1][0] or LengthRes[0][0] * 2 != LengthRes[2][0]:
        # 대각 지점 제외한 나머지 두점까지의 거리가 같고, 대각 지점과는 2배 (제곱근 안씌우고)
        return 0
    RefLength = LengthRes[0][0]
    DiagonalIdx = LengthRes[2][1]
    x, y = Points[DiagonalIdx]
    # 0번 지점을 제외, 대각 지점으로부터 각 점까지 한 변의 길이와 같아야 함.
    for i in range(1, 4):
        if i != DiagonalIdx:
            p, q = Points[i]
            if RefLength != (x - p) ** 2 + (y - q) ** 2:
                return 0

    return 1


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    TC = []
    for _ in range(TC_NUM):
        Point = []
        Point.append(tuple(map(int, input().split())))
        Point.append(tuple(map(int, input().split())))
        Point.append(tuple(map(int, input().split())))
        Point.append(tuple(map(int, input().split())))
        TC.append(Point)

    for Points in TC:
        print(is_square(Points))

    return


if __name__ == "__main__":
    solve()
