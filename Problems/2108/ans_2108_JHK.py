# https://www.acmicpc.net/problem/2108

import sys

# def getMid(cnt)
def solve():
    input = sys.stdin.readline
    N = int(input())
    InpCnt = [0] * 8001
    # 음수 input의 경우, index = 8001 + index
    # ex. input -4000 : index 4001
    # ex. input -1 : index 8000

    # 계수 정렬 counting
    sum = 0
    for _ in range(N):
        temp = int(input())
        sum += temp
        InpCnt[temp] += 1

    # 정렬 시작
    sortedData = []
    for i, v in enumerate(InpCnt[4001:]):
        # 음수 input 먼저, 작은수부터 처리
        # i 가 0부터 시작됨에 주의 (-4000 : index 0)
        for _ in range(v):
            sortedData.append(i - 4000)
            # 실제 input 값으로 decode
    for i, v in enumerate(InpCnt[:4001]):
        # 양수 input 처리
        for _ in range(v):
            sortedData.append(i)
    # 정렬 완료

    # 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
    # 그는 math 라이브러리 찾아쓰기가 귀찮았다 한다.
    if sum >= 0:
        print(int((sum / N) + 0.5))
    else:
        print(int((sum / N) - 0.5))
        # 음수 반올림은 여러 방법이 있을 수 있으므로 예제 등을 이용 해 유추
        # 본 문제에서 음수 반올림은 해당 절대값의 반올림에 -1을 곱한다.
        # ex. -0.6 -> -1
        # ex. -2.5 -> -3

    # 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    print(sortedData[N // 2])

    # 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    # 최빈값은 max(InpCnt) 의 index와 같지만,
    # 최빈값이 여러개인 경우를 위해 max 찾기를 수동으로 구현
    minCnt = 0
    minData = []
    for i, cnt in enumerate(InpCnt[4001:]):
        if cnt > minCnt:
            minCnt = cnt
            minData = [i - 4000]
        elif cnt == minCnt:
            minData.append(i - 4000)
    for i, cnt in enumerate(InpCnt[:4001]):
        if cnt > minCnt:
            minCnt = cnt
            minData = [i]
        elif cnt == minCnt:
            minData.append(i)

    if len(minData) > 1:
        print(minData[1])
        # 최빈값이 여러 개인 경우, 두번째로 작은 값 사용
    else:
        print(minData[0])

    # 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
    print(sortedData[-1] - sortedData[0])

    return


if __name__ == "__main__":
    solve()
