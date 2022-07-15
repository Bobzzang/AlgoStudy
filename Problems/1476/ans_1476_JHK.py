# https://www.acmicpc.net/problem/1476


def solve():
    E, S, M = map(int, input().split())
    E_END = 15
    S_END = 28
    M_END = 19
    E -= 1
    S -= 1
    M -= 1
    # Overflow 시 1부터 시작하는 것을 0부터 시작으로 처리 (나머지 계산과 일치하도록)
    res = S
    while True:
        if res % M_END == M:
            break
        res += S_END
    # res : S, M 을 만족하는 최소 년수
    SM_END = S_END * M_END
    # S_END와 M_END는 서로소이므로 곱은 최소공배수
    Reduce_SM = SM_END % E_END
    i = 0
    OrigRes = res
    while True:
        if res % E_END == E:
            print(OrigRes + SM_END * i + 1)
            # 위에서 0부터 시작하던 것을 다시 1부터 시작으로 처리 +1
            return
        res += Reduce_SM
        i += 1
    return


def solve2():
    E, S, M = map(int, input().split())
    E_END = 15
    S_END = 28
    M_END = 19
    E -= 1
    S -= 1
    M -= 1
    # 처음 풀이 - 이거 빼먹어서 시간초과 나는걸 모르고
    # solve()로 로직 재설계하고서야 발견.

    res = S
    while True:
        if res % E_END == E and res % M_END == M:
            print(res + 1)
            return
        res += S_END
    return


if __name__ == "__main__":
    # solve()
    solve2()
