# https://www.acmicpc.net/problem/2751

# Quick sort는 최악의 경우 O(N^2)이고,
# 이 문제의 TC는 이 최악의 경우를 상정하여 만들어져 있다 함.
# (일반적인 Quick sort로 풀리지 않는 문제)

import sys


def QuickSort(data):
    if len(data) > 1:
        left = []
        right = []
        pivot = data[len(data) // 2]
        for d in data:
            if d < pivot:
                left.append(d)
            else:  # d > pivot:
                right.append(d)
            # 겹치는 수가 없을 것이므로 pivot 과 같은 경우는 배제
        return QuickSort(left) + [pivot] + QuickSort(right)
    return data


def solve():
    input = sys.stdin.readline
    N = int(input())
    inData = []
    for _ in range(N):
        inData.append(int(input()))

    res = QuickSort(inData)
    print(*res)
    return


if __name__ == "__main__":
    solve()
