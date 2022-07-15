# https://www.acmicpc.net/problem/1051

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Arr = []
    for _ in range(N):
        Arr.append(list(map(int, input().rstrip())))

    maxSq = min(N, M)
    isNotMax = True
    while isNotMax and maxSq > 0:
        maxSq -= 1
        for i in range(N - maxSq):
            for j in range(M - maxSq):
                tempVal = Arr[i][j]
                if (
                    Arr[i + maxSq][j] == tempVal
                    and Arr[i][j + maxSq] == tempVal
                    and Arr[i + maxSq][j + maxSq] == tempVal
                ):
                    isNotMax = False
                    break

            if isNotMax == False:
                break
        if isNotMax == False:
            break

    print((maxSq + 1) ** 2)
    return


if __name__ == "__main__":
    solve()
