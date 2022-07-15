# https://www.acmicpc.net/problem/10453

import sys


def count_moving(InputStr, RefStr):
    if len(InputStr) != len(RefStr):
        # 사기문제...
        # 문제 제한 사항에 명백히 A,B의 길이가 같다는게 없어서 넣었지만
        # 없어도 잘 풀림. 즉, 변환이 불가능한 경우는 없음.
        return -1

    InputBPos = []
    for i, c in enumerate(InputStr):
        if c == "b":
            InputBPos.append(i)

    RefBPos = []
    for i, c in enumerate(RefStr):
        if c == "b":
            RefBPos.append(i)

    cnt = 0
    for idx in range(len(InputBPos)):
        cnt += abs(InputBPos[idx] - RefBPos[idx])

    return cnt


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    TC = []
    for _ in range(TC_NUM):
        TC.append(list(map(str, input().split())))

    for T in TC:
        print(count_moving(*T))
    return


if __name__ == "__main__":
    solve()
