# https://www.acmicpc.net/problem/3896

import sys


def get_prime_numbers(maxVal):
    PrimeNumFlg = [True] * 1299710

    for i in range(2, len(PrimeNumFlg)):
        if PrimeNumFlg[i] is False:
            continue
        j = i * 2
        while j < len(PrimeNumFlg):
            PrimeNumFlg[j] = False
            j += i
    PrimeNumFlg[0] = False
    PrimeNumFlg[1] = False

    PrimeNums = []
    for i, v in enumerate(PrimeNumFlg):
        if v:
            PrimeNums.append(i)
    return PrimeNums


def get_len_prime_number(PrimeNumbers, Target):
    left = 0
    right = len(PrimeNumbers)
    while left + 1 < right:
        mid = (left + right) // 2
        if PrimeNumbers[mid] > Target:
            right = mid
        elif PrimeNumbers[mid] < Target:
            left = mid
        else:
            return 0
    if PrimeNumbers[left] == Target:
        return 0
    return PrimeNumbers[left + 1] - PrimeNumbers[left]


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    TC = []
    for _ in range(TC_NUM):
        TC.append(int(input()))
    maxTC = max(TC)
    PrimeNums = get_prime_numbers(maxTC)

    for Target in TC:
        print(get_len_prime_number(PrimeNums, Target))
    return


if __name__ == "__main__":
    solve()
