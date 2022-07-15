# https://www.acmicpc.net/problem/24040

import sys


# def check_avail(V):
# 시간초과
# width = 1
# while width < V ** 0.5:
#     if V % width == 0:
#         height = V // width
#         if (width + height) % 3 == 0:
#             return "TAK"
#     width += 1
# return "NIE"


def check_avail(N):
    # 가로를 X, 세로를 Y라 할 때,
    # 1. N = XY
    # 2. (2X+2Y) % 3 == 0 을 만족하는 0 이상의 정수가 있는지 확인
    # 2번 식을 만족하는 X, Y의 조합은
    # 1) X = 3P, Y = 3Q
    # 2) X = 3P+1, Y= 3Q+2
    # 3) X = 3P+2, Y= 3Q+1   ... P, Q는 0 이상의 정수
    # 위 3개 경우 뿐이며, X Y의 구분이 없으므로 2,3은 중복 케이스이다.
    # 이 경우, 각 경우에 대해 1번 식을 계산하면
    # 1) N = 9PQ  (N은 9의 배수)
    # 2) N = 9PQ + 6P + 3Q + 2  (P=0이라 가정하면, N은 3으로 나누었을 때 나머지가 2인 모든 수)
    if N % 3 == 2 or N % 9 == 0:
        return "TAK"
    return "NIE"


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        TC.append(int(input()))
    for Vol in TC:
        print(check_avail(Vol))
    return


if __name__ == "__main__":
    solve()
