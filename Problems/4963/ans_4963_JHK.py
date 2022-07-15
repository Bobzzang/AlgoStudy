# https://www.acmicpc.net/problem/4963

import sys

sys.setrecursionlimit(2500)
# 최대 크기인 경우, 50x50 만큼 재귀가 가능하므로 Recursion Limit 변경
# pypy는 recursion limit가 c-python보다 커서 해당 내용 없이 성공


def make_land_to_sea(S_Map, W, H, idx_row, idx_col):
    if idx_row < 0:
        return
    if idx_col < 0:
        return
    if idx_row >= H:
        return
    if idx_col >= W:
        return
    if S_Map[idx_row][idx_col] == 0:
        return

    S_Map[idx_row][idx_col] = 0

    make_land_to_sea(S_Map, W, H, idx_row - 1, idx_col - 1)
    make_land_to_sea(S_Map, W, H, idx_row - 1, idx_col)
    make_land_to_sea(S_Map, W, H, idx_row - 1, idx_col + 1)

    make_land_to_sea(S_Map, W, H, idx_row, idx_col - 1)
    # make_land_to_sea(S_Map, W, H, idx_row, idx_col)
    make_land_to_sea(S_Map, W, H, idx_row, idx_col + 1)

    make_land_to_sea(S_Map, W, H, idx_row + 1, idx_col - 1)
    make_land_to_sea(S_Map, W, H, idx_row + 1, idx_col)
    make_land_to_sea(S_Map, W, H, idx_row + 1, idx_col + 1)
    return


def get_num_island(S_Map, W, H):
    cnt = 0
    for idx_row in range(H):
        for idx_col in range(W):
            if S_Map[idx_row][idx_col] == 1:
                cnt += 1
                make_land_to_sea(S_Map, W, H, idx_row, idx_col)
    return cnt


def solve():
    input = sys.stdin.readline
    Maps = []
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        S_Map = []
        for _ in range(H):
            S_Map.append(list(map(int, input().split())))
        Maps.append(S_Map)

    for S_Map in Maps:
        W = len(S_Map[0])
        H = len(S_Map)
        print(get_num_island(S_Map, W, H))
    return


if __name__ == "__main__":
    solve()
