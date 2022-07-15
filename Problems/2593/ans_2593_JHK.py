# https://www.acmicpc.net/problem/2583

import sys

sys.setrecursionlimit(10002)
# Recursion Limit - N*M 최댓값 : 10000
# 기타 함수 호출 margin


def fill_space(N, Space, sq):
    x1, y1, x2, y2 = sq
    for x in range(x1, x2):
        for y in range(y1, y2):
            Space[x + y * N] = 2
            # 2 is wall
    return


def get_room_area(StartIdx, Space, N, M):
    # Space[StartIdx] = 1
    # 1 is visited
    res_area = 1
    x, y = StartIdx % N, StartIdx // N
    if x > 0:
        TargetIdx = x - 1 + y * N
        if Space[TargetIdx] == 0:
            Space[TargetIdx] = 1
            res_area += get_room_area(TargetIdx, Space, N, M)
    if x < N - 1:
        TargetIdx = x + 1 + y * N
        if Space[TargetIdx] == 0:
            Space[TargetIdx] = 1
            res_area += get_room_area(TargetIdx, Space, N, M)
    if y > 0:
        TargetIdx = x + (y - 1) * N
        if Space[TargetIdx] == 0:
            Space[TargetIdx] = 1
            res_area += get_room_area(TargetIdx, Space, N, M)
    if y < M - 1:
        TargetIdx = x + (y + 1) * N
        if Space[TargetIdx] == 0:
            Space[TargetIdx] = 1
            res_area += get_room_area(TargetIdx, Space, N, M)
    return res_area


def solve():
    input = sys.stdin.readline
    M, N, K = map(int, input().split())
    Squares = [tuple(map(int, input().split())) for _ in range(K)]
    Space = [0] * (M * N)
    for sq in Squares:
        fill_space(N, Space, sq)
    res = []
    for i in range(len(Space)):
        if Space[i] == 0:
            Space[i] = 1
            res.append(get_room_area(i, Space, N, M))

    res.sort()
    print(len(res))
    print(*res)
    return


if __name__ == "__main__":
    solve()
