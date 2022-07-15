# https://www.acmicpc.net/problem/1004

import sys


def check_point(x, y, p, q, r):
    if r ** 2 > ((x - p) ** 2 + (y - q) ** 2):
        return 1
    return -1


def count_crossing(StartPoint, EndPoint, Planets):
    count = 0
    for p in Planets:
        if check_point(*StartPoint, *p) * check_point(*EndPoint, *p) < 0:
            count += 1
    return count


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        x, y, p, q = map(int, input().split())
        StartPoint = [x, y]
        EndPoint = [p, q]
        NumPlanet = int(input())
        Planets = []
        for _ in range(NumPlanet):
            Planets.append(list(map(int, input().split())))
        TC.append([StartPoint, EndPoint, Planets])
    for t in TC:
        print(count_crossing(*t))
    return


if __name__ == "__main__":
    solve()
