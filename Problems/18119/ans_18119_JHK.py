# https://www.acmicpc.net/problem/18119

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Words = [input().rstrip() for _ in range(N)]
    Quaries = [ord(input().split()[1]) - ord("a") for _ in range(M)]
    # command 가 1인지 2인지는 중요하지 않음.

    WordMask = []
    for w in Words:
        mask = 0
        for c in w:
            mask |= 1 << (ord(c) - ord("a"))
        WordMask.append(mask)

    Remember = (1 << (ord("z") - ord("a") + 1)) - 1
    for c in Quaries:
        Remember ^= 1 << c
        cnt = 0
        for w in WordMask:
            if w == w & Remember:
                cnt += 1
        print(cnt)
    return


if __name__ == "__main__":
    solve()
