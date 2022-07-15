# https://www.acmicpc.net/problem/4307

import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def get_min_time(L, ants):
    # 막대 정중앙에서 가장 가까운 개미가 자신으로부터 가까운 막대 끝까지 충돌 없이 가는 경우
    # 가장 빠른 시간 내에 막대 끝에 도달 할 수 있다.
    medium = L / 2
    DiffMedMin = L

    for i, v in enumerate(ants):
        if DiffMedMin > abs(medium - v):
            DiffMedMin = abs(medium - v)
            MinVal = v

    if MinVal < L - MinVal:
        return MinVal
    return L - MinVal


def get_max_time(L, ants):
    # 양 끝의 개미 중 막대 끝에서 보다 가까이 있는 개미를 A, 반대쪽 끝에 있는 개미를 B라 할 때
    # A를 안쪽으로 보내고, B를 포함한 나머지 개미를 그 반대쪽으로 보낼 경우
    # 연쇄적으로 충돌이 일어나는데, 이 때 B가 충돌 (B 옆의 개미와) 충돌하는 위치는
    # A, B만 존재 할 경우의 위치와 같으며, 그 위치는 A-B 사이의 중간점이다. (이동속도가 같기 때문)
    # 따라서 최대 시간은 A-B에서 충돌점까지의 왕복시간 (즉 A-B 구간 이동시간) + A의 초기위치로부터 막대 끝까지 가는 시간과 같다.
    if ants[0] > L - ants[-1]:
        return ants[-1]  # L - (L - ants[-1])
    return L - ants[0]


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    TC = []
    for _ in range(TC_NUM):
        L, N = map(int, input().split())
        ants = []
        for _ in range(N):
            ants.append(int(input()))ㅉ
        TC.append([L, merge_sort(ants)])

    for T in TC:
        print(get_min_time(*T), get_max_time(*T))
    return


if __name__ == "__main__":
    solve()
