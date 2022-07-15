# https://www.acmicpc.net/problem/1052


def cnt_bottleNum(Ref):
    cnt = 0
    mask = 1
    while mask <= Ref:
        if Ref & mask == mask:
            cnt += 1
        mask = mask << 1
    return cnt


def solve():
    N, K = map(int, input().split())
    Res = N
    while True:
        BottleNum = cnt_bottleNum(Res)
        if BottleNum <= K:
            print(Res - N)
            return
        mask = 1
        while Res >= mask:
            if Res & mask == mask:
                Res += mask
                break
            mask = mask << 1


if __name__ == "__main__":
    solve()
