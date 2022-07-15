# https://www.acmicpc.net/problem/2210

import sys


def track_board(board, start, depth):
    x, y = start % 5, start // 5
    if depth >= 6:
        return [""]
    res = []
    defNum = str(board[start])
    if x != 0:
        for nums in track_board(board, y * 5 + x - 1, depth + 1):
            res.append(defNum + nums)
    if y != 0:
        for nums in track_board(board, (y - 1) * 5 + x, depth + 1):
            res.append(defNum + nums)
    if x != 4:
        for nums in track_board(board, y * 5 + x + 1, depth + 1):
            res.append(defNum + nums)
    if y != 4:
        for nums in track_board(board, (y + 1) * 5 + x, depth + 1):
            res.append(defNum + nums)

    return res


def solve():
    input = sys.stdin.readline
    board = []
    for _ in range(5):
        board += list(map(int, input().split()))
    res = set()
    for i in range(25):
        for nums in track_board(board, i, 0):
            res.add(nums)

    print(len(res))
    return


if __name__ == "__main__":
    solve()
