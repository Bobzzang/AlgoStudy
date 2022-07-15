# https://www.acmicpc.net/problem/10972

import sys


def solve2():
    input = sys.stdin.readline
    N = int(input())
    RefNum = list(map(int, input().split()))
    Used = [True] * (N + 1)

    Used[RefNum[N - 1]] = False
    IsEnd = True
    for i in range(N - 2, -1, -1):
        Used[RefNum[i]] = False
        if RefNum[i] < RefNum[i + 1]:
            IsEnd = False
            TargetIdx = i
            # 뒤에서부터 탐색하여 앞의 값이 더 작은 경우에 대해,
            # 해당 위치부터 순열이 조정됨.
            # ex. 2 4 5 3 1 일 경우, i=1(4) 부터 순열이 조정됨.
            break

    if IsEnd:
        # 수열이 내림차순인 경우
        print(-1)
        return

    for idx in range(TargetIdx):
        print(RefNum[idx], end=" ")
        # TargetIdx 이전까지는 기존 순열을 print

    UsedIdx = RefNum[TargetIdx] + 1
    # TargetIdx 위치의 값이 증가해야 하므로,
    # TargetIdx 보다 크고 가장 가까운 Unused 값 탐색
    while True:
        if Used[UsedIdx] == False:
            Used[UsedIdx] = True
            print(UsedIdx, end=" ")
            break
        UsedIdx += 1

    for i, v in enumerate(Used):
        if v == False:
            print(i, end=" ")
            # 나머지 Unused 값을 작은 값부터 print

    print()
    return


def solve():
    # 대강 풀고, solve2로 가독성 있게 정리함.
    input = sys.stdin.readline
    N = int(input())
    RefNum = list(map(int, input().split()))
    Used = [True] * (N + 1)

    Used[RefNum[N - 1]] = False
    for i in range(N - 2, -1, -1):
        Used[RefNum[i]] = False
        if RefNum[i] < RefNum[i + 1]:
            for j in range(RefNum[i] + 1, N + 1):
                if Used[j] == False:
                    Used[j] = True
                    RefNum[i] = j
                    break
            for j in range(i + 1, N):
                for p in range(1, N + 1):
                    if Used[p] == False:
                        RefNum[j] = p
                        Used[p] = True
                        break
            for p in RefNum:
                print(p, end=" ")
            print()
            return
    print(-1)

    return


if __name__ == "__main__":
    solve2()
