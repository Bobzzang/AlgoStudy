# https://www.acmicpc.net/problem/1520

import sys


def getPathNum(data, pathNum, rowi, colj):
    # 아래 재귀함수에 memoization 로직 추가
    if pathNum[rowi][colj] != None:
        return pathNum[rowi][colj]
        # load memo

    ref = data[rowi][colj]
    res = 0
    if rowi > 0:
        if ref < data[rowi - 1][colj]:
            # check UP
            res += getPathNum(data, pathNum, rowi - 1, colj)
    if rowi < N - 1:
        if ref < data[rowi + 1][colj]:
            # check DOWN
            res += getPathNum(data, pathNum, rowi + 1, colj)
    if colj > 0:
        if ref < data[rowi][colj - 1]:
            # check LEFT
            res += getPathNum(data, pathNum, rowi, colj - 1)
    if colj < M - 1:
        if ref < data[rowi][colj + 1]:
            # check RIGHT
            res += getPathNum(data, pathNum, rowi, colj + 1)

    pathNum[rowi][colj] = res
    # memoization
    return res


# 일반 재귀로는 여기까지 해도 답은 맞음. 재귀제한에 걸림.
# def getPathNum(data, rowi, colj):
#     ref = data[rowi][colj]
#     if rowi == 0 and colj == 0:
#         res = 1
#     else:
#         res = 0
#     if rowi > 0:
#         if ref < data[rowi - 1][colj]:
#             # UP
#             res += getPathNum(data, rowi - 1, colj)
#     if rowi < N - 1:
#         if ref < data[rowi + 1][colj]:
#             # DOWN
#             res += getPathNum(data, rowi + 1, colj)
#     if colj > 0:
#         if ref < data[rowi][colj - 1]:
#             # LEFT
#             res += getPathNum(data, rowi, colj - 1)
#     if colj < M - 1:
#         if ref < data[rowi][colj + 1]:
#             # RIGHT
#             res += getPathNum(data, rowi, colj + 1)
#     return res


def solve():
    global N, M
    input = sys.stdin.readline
    N, M = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(tuple(map(int, input().split())))

    pathNum = [[None] * M for _ in range(N)]
    pathNum[0][0] = 1
    # pathNum : 해당 위치에 올 수 있는 경우의 수 - 이 시점에선 시작위치밖에 모름.
    # 값을 알게 되면 None -> integer로 처리될 것.

    """
    res = getPathNum(data, N - 1, M - 1)
    # 그냥 재귀 돌릴 경우, Recursion 횟수 제한에 걸림.
    """

    # 적당히 재귀 횟수를 줄일 수 있을만큼만 Bottom-up
    for i in range(min(N, M)):
        for j in range(i + 1):
            getPathNum(data, pathNum, j, i - j)

    # 최종 결과는 Top-down으로 재귀로 계산
    res = getPathNum(data, pathNum, N - 1, M - 1)

    print(res)
    return


if __name__ == "__main__":
    solve()
