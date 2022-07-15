# https://www.acmicpc.net/problem/4375

import sys


def solve():
    Numbers = [int(x.rstrip()) for x in sys.stdin.readlines()]
    for n in Numbers:
        i = len(str(n))
        modNum = int("1" * (len(str(n)))) % n
        while modNum != 0:
            modNum *= 10
            modNum += 1
            modNum %= n
            i += 1
        print(i)
    return


if __name__ == "__main__":
    solve()
