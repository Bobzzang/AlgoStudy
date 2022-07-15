# https://www.acmicpc.net/problem/1439


def solve():
    S = input()
    C_Old = "-"
    zero_cnt = 0
    one_cnt = 0
    for C in S:
        if C != C_Old:
            if C == "0":
                zero_cnt += 1
            else:
                one_cnt += 1
            C_Old = C
    if zero_cnt > one_cnt:
        print(one_cnt)
    else:
        print(zero_cnt)
    return


if __name__ == "__main__":
    solve()
