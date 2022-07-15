# https://www.acmicpc.net/problem/11049

import sys

MAXDEF = (2 ** 31) - 1
mat = []
memo = []
# dic = {}


def getSumMin(start, end):
    if memo[start][end] != None:
        return memo[start][end]
    if end - start == 0:
        memo[start][end] = 0
        return 0
    if end - start == 1:
        memo[start][end] = mat[start][0] * mat[start][1] * mat[end][1]
        return memo[start][end]
    minval = MAXDEF
    for mid in range(start, end):
        temp = (
            getSumMin(start, mid)
            + getSumMin(mid + 1, end)
            + mat[start][0] * mat[mid][1] * mat[end][1]
            # 모든 행렬곱은 두 행렬의 곱으로 정리된다.
            # 두 행렬로 만드는 경우의 수를 탐색 + 두 행렬의 곱을 할 경우 발생하는 비용
            # 나누어진 행렬은 재귀적으로 다시 나눌 수 있다.
        )
        if temp < minval:
            minval = temp
            # 모든 경우 중, 최소 비용의 경우를 return
    memo[start][end] = minval
    return minval


# Dictionary 를 memo로 이용하도록 초기 구현 - Time Out
# Index가 명백할 경우에는 dictionary가 조금 더 느린 것 같다.

# def getSumMin(start, end):
#     if (start, end) in dic:
#         return dic[start, end]
#     if end - start == 0:
#         dic[start, end] = 0
#         return 0
#     if end - start == 1:
#         dic[start, end] = mat[start][0] * mat[start][1] * mat[end][1]
#         return dic[start, end]
#     minval = MAXDEF
#     for mid in range(start, end):
#         temp = (
#             getSumMin(start, mid)
#             + getSumMin(mid + 1, end)
#             + mat[start][0] * mat[mid][1] * mat[end][1]
#         )
#         if temp < minval:
#             minval = temp
#     dic[start, end] = minval
#     return minval


def solve():
    input = sys.stdin.readline
    N = int(input())

    for _ in range(N):
        mat.append(tuple(map(int, input().split())))
        memo.append([None] * N)

    # Bottom - up
    # 안해도 재귀 제한에 걸리지 않는 갯수 (max 500)
    # 어쨋든 함수 call 횟수가 많아져서인지 약간 시간이 늘어남.
    # Top - Down: 1500ms
    # Bottom - up : 1440ms
    # for refLength in range(len(mat)):
    #     for startIdx in range(len(mat) - refLength):
    #         getSumMin(startIdx, startIdx + refLength)

    print(getSumMin(0, len(mat) - 1))
    return


if __name__ == "__main__":
    solve()
