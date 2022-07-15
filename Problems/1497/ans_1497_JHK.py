# https://www.acmicpc.net/problem/1497

import sys


def check_cover(N, GuitarSelect, SongSet):
    GuitarCnt = bin(GuitarSelect).count("1")
    i = 0
    res = 0
    while GuitarSelect != 0:
        if GuitarSelect % 2 == 1:
            res |= SongSet[i]
        GuitarSelect //= 2
        i += 1
    return GuitarCnt, bin(res).count("1")


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    SongSet = []
    for _ in range(N):
        mask = 0
        for i, song in enumerate(input().split()[1]):
            if song == "Y":
                mask |= 1 << i
        SongSet.append(mask)
    SongMax = 0
    GuitarMin = N + 1
    for i in range(2 ** N):
        guitarCnt, SongCnt = check_cover(N, i, SongSet)
        if SongCnt > SongMax:
            GuitarMin = guitarCnt
            SongMax = SongCnt
        elif SongCnt == SongMax:
            if GuitarMin > guitarCnt:
                GuitarMin = guitarCnt

    if SongMax == 0:
        print(-1)
    else:
        print(GuitarMin)
    return


if __name__ == "__main__":
    solve()
