# https://www.acmicpc.net/problem/15787

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Train = [0] * N
    FullMask = 0b11111111111111111111
    for _ in range(M):
        TempCmd = list(map(int, input().split()))
        if TempCmd[0] == 1 or TempCmd[0] == 2:
            Cmd, i, x = TempCmd
            x -= 1
        else:
            Cmd, i = TempCmd
        i -= 1

        if Cmd == 1:
            TempMask = 0b1 << x
            if Train[i] & TempMask != TempMask:
                Train[i] += TempMask
            continue

        if Cmd == 2:
            TempMask = 0b1 << x
            if Train[i] & TempMask == TempMask:
                Train[i] -= TempMask
            continue

        if Cmd == 3:
            Train[i] = Train[i] << 1 & FullMask
            continue

        if Cmd == 4:
            Train[i] = Train[i] >> 1
            continue

    cnt = 0
    res = []
    for t in Train:
        if t not in res:
            res.append(t)
            cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
