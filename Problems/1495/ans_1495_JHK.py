# https://www.acmicpc.net/problem/1495


def solve():
    N, S, M = map(int, input().split())
    VolFix = list(map(int, input().split()))
    Ref = [False] * (M + 1)
    Tar = [False] * (M + 1)
    Ref[S] = True
    for vol in VolFix:
        for i, v in enumerate(Ref):
            if v:
                Ref[i] = False
                if i - vol >= 0:
                    Tar[i - vol] = True
                if i + vol <= M:
                    Tar[i + vol] = True
        Ref, Tar = Tar, Ref
    i = M
    while i >= 0:
        if Ref[i]:
            print(i)
            return
        i -= 1
    print(-1)
    return


if __name__ == "__main__":
    solve()
