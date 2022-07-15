# https://www.acmicpc.net/problem/18233

import sys
import itertools


def solve():
    input = sys.stdin.readline
    N, P, E = map(int, input().split())
    Members = [list(map(int, input().split())) for _ in range(N)]
    Index = [x for x in range(N)]
    Res = [0] * N
    Selected = list(itertools.combinations(Index, P))
    is_selectable = False
    for sel in Selected:
        MinSum = 0
        MaxSum = 0
        for i in sel:
            MinSum += Members[i][0]
            MaxSum += Members[i][1]
        if E >= MinSum and E <= MaxSum:
            is_selectable = True
            break
    if is_selectable == False:
        print(-1)
        return
    for i in sel:
        Res[i] += Members[i][0]
        E -= Members[i][0]
    for i in sel:
        if Members[i][1] - Res[i] < E:
            E -= Members[i][1] - Res[i]
            Res[i] = Members[i][1]
        else:
            Res[i] += E
            E = 0
    print(*Res)
    return


if __name__ == "__main__":
    solve()
