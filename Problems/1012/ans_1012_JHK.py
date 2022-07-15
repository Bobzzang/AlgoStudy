# https://www.acmicpc.net/problem/1012

import sys


def checkAround(ground, BatchuStack, M, N, i, j):
    if i > 0:
        if ground[j][i - 1] == 1:
            BatchuStack.append((i - 1, j))
            checkBatchuGroup_DFS(ground, M, N, i - 1, j)
    if i < M - 1:
        if ground[j][i + 1] == 1:
            BatchuStack.append((i + 1, j))
    if j > 0:
        if ground[j - 1][i] == 1:
            BatchuStack.append((i, j - 1))
    if j < N - 1:
        if ground[j + 1][i] == 1:
            BatchuStack.append((i, j + 1))
    return


def checkBatchuGroup_BFS(ground, BatchuStack, M, N, i, j):
    ground[j][i] = 0
    checkAround(ground, BatchuStack, M, N, i, j)
    while BatchuStack != []:
        x, y = BatchuStack.pop()
        ground[y][x] = 0

        checkAround(ground, BatchuStack, M, N, x, y)

    return


def checkBatchuGroup_DFS(ground, M, N, i, j):
    # K <= 2500 이므로, 최악의 경우 RecursionError 발생 가능
    ground[j][i] = 0
    if i > 0:
        if ground[j][i - 1] == 1:
            checkBatchuGroup_DFS(ground, M, N, i - 1, j)
    if i < M - 1:
        if ground[j][i + 1] == 1:
            checkBatchuGroup_DFS(ground, M, N, i + 1, j)
    if j > 0:
        if ground[j - 1][i] == 1:
            checkBatchuGroup_DFS(ground, M, N, i, j - 1)
    if j < N - 1:
        if ground[j + 1][i] == 1:
            checkBatchuGroup_DFS(ground, M, N, i, j + 1)

    return


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    res = []
    for _ in range(TC_NUM):
        M, N, K = map(int, input().split())
        ground = [[0] * M for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().split())
            ground[y][x] = 1
        cnt = 0
        for i in range(M):
            for j in range(N):
                if ground[j][i] == 1:
                    cnt += 1
                    BatchuStack = []
                    # checkBatchuGroup_DFS(ground, M, N, i, j)
                    checkBatchuGroup_BFS(ground, BatchuStack, M, N, i, j)
        res.append(cnt)
    for r in res:
        print(r)
    return


if __name__ == "__main__":
    solve()
