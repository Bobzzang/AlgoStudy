# https://www.acmicpc.net/problem/10830

import sys


def matMul(matA, matB):
    global N
    res = []
    for r1 in range(N):
        tempRow = []
        for r2 in range(N):
            el = 0
            for c in range(N):
                el += matA[r1][c] * matB[c][r2]
            if el >= 1000:
                el %= 1000
            tempRow.append(el)
        res.append(tempRow)
    return res


def solve():
    global N
    input = sys.stdin.readline
    N, B = map(int, input().split())
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))

    ans = []
    for i in range(N):
        tempRow = []
        for j in range(N):
            if i == j:
                e = 1
            else:
                e = 0
            tempRow.append(e)
        ans.append(tempRow)
    # start from identity matrix
    while B != 0:
        if B % 2 == 0:
            mat = matMul(mat, mat)
            B = B // 2
        else:
            ans = matMul(mat, ans)
            B -= 1

    for r in ans:
        print(" ".join([str(x) for x in r]))
    return


if __name__ == "__main__":
    solve()
