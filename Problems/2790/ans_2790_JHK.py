# https://www.acmicpc.net/problem/2790

import sys


def merge(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])
    return merge(left, right)


def count_winner(Scores):
    N = len(Scores)
    WinningScore = 0
    for i, v in enumerate(Scores):
        if v + N - i > WinningScore:
            # 경우에 따라 우승을 할 수 있는 최저 점수를 찾음.
            # 마지막 레이스에서 최저점자부터 순서대로 들어왔을 때
            # 우승자의 점수는 모든 경우에서 우승이 가능할수도 있는 최저점이다.
            # (기존 고점수자의 점수 획득을 최대한 막는 방법)
            WinningScore = v + N - i
    cnt = 0
    for v in Scores:
        if v + N >= WinningScore:
            # 위에서 구한 WinningScore에 대해,
            # 모든 선수가 1등을 하였을 때 WinningScore를 넘긴다면
            # 경우에 따라 우승이 가능하다.
            cnt += 1
    return cnt


def solve():
    input = sys.stdin.readline
    N = int(input())
    Scores = []
    for _ in range(N):
        Scores.append(int(input()))
    Scores = merge_sort(Scores)
    print(count_winner(Scores))
    return


if __name__ == "__main__":
    solve()
