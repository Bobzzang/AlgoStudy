# https://www.acmicpc.net/problem/10252

# 사이클 - 다 돌고 제자리로 돌아와야 한다
# 사실 torus나 그냥 사각 그리드나 동일한 궤적으로 가능

import sys


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        TC.append(list(map(int, input().split())))

    for torus in TC:
        print(1)
        # 항상 1
        N, M = torus

        if N % 2 == 0:
            for i in range(N):
                if i % 2 == 0:
                    for j in range(M):
                        print(f"({i},{j})")

                else:
                    for j in range(M - 1, -1, -1):
                        print(f"({i},{j})")
        else:
            for i in range(N):
                if i % 2 == 0:
                    for j in range(M - 1):
                        print(f"({i},{j})")
                else:
                    for j in range(M - 2, -1, -1):
                        print(f"({i},{j})")
            j = M - 1
            for i in range(N - 1, -1, -1):
                print(f"({i},{j})")

    return


if __name__ == "__main__":
    solve()
