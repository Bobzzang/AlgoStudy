# https://www.acmicpc.net/problem/1629

# res  = C*X + d
# res * A = A*C*X + d*A


def solve():
    A, B, C = map(int, input().split())
    fixA = A
    res = 1
    while B != 0:
        if B % 2 == 0:
            fixA = fixA ** 2
            if fixA > C:
                fixA %= C
            B = B // 2
        else:
            B -= 1
            res *= fixA
            if res > C:
                res %= C

    print(res)
    return


if __name__ == "__main__":
    solve()
