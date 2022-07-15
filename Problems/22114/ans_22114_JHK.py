# https://www.acmicpc.net/problem/22114


def solve():
    N, K = map(int, input().split())
    Blocks = list(map(int, input().split()))
    MaxStep = 0
    StartBlockIdx = 0
    while MaxStep < len(Blocks) - StartBlockIdx:
        j = StartBlockIdx
        cnt = 0
        is_jumped = False
        while j < len(Blocks):
            if K >= Blocks[j]:
                cnt += 1
            else:
                if is_jumped == True:
                    break
                else:
                    cnt += 1
                    is_jumped = True
            j += 1
        MaxStep = max(MaxStep, cnt)
        StartBlockIdx += 1

    print(MaxStep + 1)
    return


if __name__ == "__main__":
    solve()
