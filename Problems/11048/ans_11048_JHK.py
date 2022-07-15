# https://www.acmicpc.net/problem/11048

import sys


def cnt_max_candy(x, y, maze, candy):
    if candy[y][x] != -1:
        return candy[y][x]
    maxcandy = 0
    if x > 0 and y > 0:
        maxcandy = max(maxcandy, cnt_max_candy(x - 1, y - 1, maze, candy))
    if x > 0:
        maxcandy = max(maxcandy, cnt_max_candy(x - 1, y, maze, candy))
    if y > 0:
        maxcandy = max(maxcandy, cnt_max_candy(x, y - 1, maze, candy))
    candy[y][x] = maxcandy + maze[y][x]
    return maxcandy


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(N)]
    candy = [[-1] * M for _ in range(N)]
    candy[0][0] = maze[0][0]
    i = 1
    while i < N + M - 1:
        for x in range(i + 1):
            y = i - x
            if x < M and y < N:
                cnt_max_candy(x, y, maze, candy)
        i += 1
    print(cnt_max_candy(M - 1, N - 1, maze, candy))
    return


if __name__ == "__main__":
    solve()
