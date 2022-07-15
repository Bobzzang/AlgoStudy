# https://www.acmicpc.net/problem/16956

import sys


def check_around(i, j, Pos, R, C):
    if Pos[i][j] == "W":
        if i > 0:
            if Pos[i - 1][j] == "S":
                return True
            if Pos[i - 1][j] == ".":
                Pos[i - 1][j] = "D"

        if i < R - 1:
            if Pos[i + 1][j] == "S":
                return True
            if Pos[i + 1][j] == ".":
                Pos[i + 1][j] = "D"

        if j > 0:
            if Pos[i][j - 1] == "S":
                return True
            if Pos[i][j - 1] == ".":
                Pos[i][j - 1] = "D"

        if j < C - 1:
            if Pos[i][j + 1] == "S":
                return True
            if Pos[i][j + 1] == ".":
                Pos[i][j + 1] = "D"
    return False


def solve():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    Pos = []
    for _ in range(R):
        Pos.append(list(input().rstrip()))
    for i in range(R):
        for j in range(C):
            if check_around(i, j, Pos, R, C):
                print(0)
                return
    print(1)
    for r in Pos:
        print("".join(r))

    return


if __name__ == "__main__":
    solve()
