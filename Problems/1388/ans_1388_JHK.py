# https://www.acmicpc.net/problem/1388

import sys


def cnt_board(Tiles, is_visited, N, M, idx):
    if is_visited[idx]:
        return 0
    x, y = idx % M, idx // M
    is_visited[idx] = True
    if Tiles[idx] == "-":
        if x < M - 1 and Tiles[idx] == Tiles[idx + 1]:
            return cnt_board(Tiles, is_visited, N, M, idx + 1)
        else:
            return 1
    else:
        if y < N - 1 and Tiles[idx] == Tiles[idx + M]:
            return cnt_board(Tiles, is_visited, N, M, idx + M)
        else:
            return 1


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Tiles = ""
    for _ in range(N):
        Tiles += input().rstrip()
    is_visited = [False] * len(Tiles)
    cnt = 0
    for i in range(N * M):
        cnt += cnt_board(Tiles, is_visited, N, M, i)
        a = 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
