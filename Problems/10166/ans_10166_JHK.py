# https://www.acmicpc.net/problem/10166


def solve():
    D1, D2 = map(int, input().split())
    res = {}
    cnt = 0
    if D1 > D2 // 2:
        start = D1
    else:
        start = D2 // 2
    for v in range(start, D2 + 1):
        temp = []
        for a in range(1, v + 1):
            p = a
            b = v
            while b % a != 0:
                a, b = b % a, a
            if v // a not in res:
                temp.append(v // a)
                cnt += 1
        for t in temp:
            res[t] = 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
