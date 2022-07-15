# https://www.acmicpc.net/problem/16937

import sys


def get_area(stickerset):
    sticker1, sticker2 = stickerset
    return sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1]


def sort_by_sum(arr):
    # merge_sort
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            Area_Left = get_area(left[i])
            Area_Right = get_area(right[j])
            if Area_Left > Area_Right:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    return merge(sort_by_sum(arr[: len(arr) // 2]), sort_by_sum(arr[len(arr) // 2 :]))


def is_available(H, W, stickerset):
    # if H < W:
    #     # H will be always bigger than W
    #     H, W = W, H
    st1, st2 = stickerset

    tempX = max(st1[0], st2[0])
    tempY = st1[1] + st2[1]
    if (tempX <= W and tempY <= H) or (tempX <= H and tempY <= W):
        return True

    tempX = max(st1[1], st2[0])
    tempY = st1[0] + st2[1]
    if (tempX <= W and tempY <= H) or (tempX <= H and tempY <= W):
        return True

    tempX = max(st1[0], st2[1])
    tempY = st1[1] + st2[0]
    if (tempX <= W and tempY <= H) or (tempX <= H and tempY <= W):
        return True

    tempX = max(st1[1], st2[1])
    tempY = st1[0] + st2[0]
    if (tempX <= W and tempY <= H) or (tempX <= H and tempY <= W):
        return True

    return False


def solve():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    N = int(input())
    Stickers = [tuple(map(int, input().split())) for _ in range(N)]
    Combinations = []
    for i in range(len(Stickers)):
        for j in range(i + 1, len(Stickers)):
            Combinations.append([Stickers[i], Stickers[j]])
    Sorted_Comb = sort_by_sum(Combinations)
    for stickerset in Sorted_Comb:
        if is_available(H, W, stickerset):
            print(get_area(stickerset))
            return
    print(0)
    return


if __name__ == "__main__":
    solve()
