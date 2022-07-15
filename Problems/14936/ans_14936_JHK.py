# https://www.acmicpc.net/problem/14936


def get_available(Sels, N, M):
    res = []
    for sel in Sels:
        cnt = 0
        cnt += int(sel[0]) * N
        cnt += int(sel[1]) * (N // 2)
        cnt += int(sel[2]) * ((N + 1) // 2)
        cnt += int(sel[3]) * ((N + 2) // 3)
        if cnt <= M:
            res.append(sel)
    return res


def flip_All(r, N):
    for i in range(N):
        r ^= 1 << i
    return r


def flip_Even(r, N):
    for i in range(N):
        if i % 2 == 1:
            r ^= 1 << i
    return r


def flip_Odd(r, N):
    for i in range(N):
        if i % 2 == 0:
            r ^= 1 << i
    return r


def flip_3rd(r, N):
    for i in range(N):
        if i % 3 == 0:
            r ^= 1 << i
    return r


def solve():
    N, M = map(int, input().split())
    Sels = [format(x, "04b") for x in range(2 ** 4 - 1)]
    Sels = get_available(Sels, N, M)
    N = min(20, N)
    Res = set()

    for sel in Sels:
        r = 0
        if int(sel[0]):
            r = flip_All(r, N)
        if int(sel[1]):
            r = flip_Even(r, N)
        if int(sel[2]):
            r = flip_Odd(r, N)
        if int(sel[3]):
            r = flip_3rd(r, N)
        Res.add(r)
    print(len(Res))
    return


if __name__ == "__main__":
    solve()
