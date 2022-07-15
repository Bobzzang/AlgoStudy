# https://www.acmicpc.net/problem/20438

import sys


def solve():
    input = sys.stdin.readline
    N, K, Q, M = map(int, input().split())
    Inhibits = list(map(int, input().split()))
    StartNums = list(map(int, input().split()))
    TC = [tuple(map(int, input().split())) for _ in range(M)]
    Sleeping = [False] * (N + 3)
    Attended = [False] * (N + 3)
    for idx in Inhibits:
        Sleeping[idx] = True

    for idx in StartNums:
        if Sleeping[idx] == False:
            Attended[idx] = True

    for idx in range(3, N + 3):
        if Attended[idx]:
            accSum = idx
            while accSum < N + 3:
                if Sleeping[accSum] == False:
                    Attended[accSum] = True
                accSum += idx

    PSum = 0
    AttendCnt = [0, 0, 0]
    for i in range(3, N + 3):
        if Attended[i] == False:
            PSum += 1
        AttendCnt.append(PSum)

    for S, E in TC:
        print(AttendCnt[E] - AttendCnt[S - 1])
    return


if __name__ == "__main__":
    solve()
