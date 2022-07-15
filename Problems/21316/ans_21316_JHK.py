# https://www.acmicpc.net/problem/21316

import sys


def solve():
    input = sys.stdin.readline
    stars = [[] for _ in range(13)]
    for _ in range(12):
        a, b = map(int, input().split())
        stars[a].append(b)
        stars[b].append(a)

    for i, star in enumerate(stars):
        if len(star) == 3:
            CheckResult = [False, False, False]
            for s in star:
                if len(stars[s]) == 1:
                    CheckResult[0] = True
                if len(stars[s]) == 2:
                    CheckResult[1] = True
                if len(stars[s]) == 3:
                    CheckResult[2] = True
            if all(CheckResult):
                print(i)
                return


if __name__ == "__main__":
    solve()
