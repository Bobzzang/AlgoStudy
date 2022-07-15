# https://www.acmicpc.net/problem/6588

import sys


def is_prime(i, PNums):
    for idx in range(2, i):
        if idx ** 2 > i:
            return True
        if PNums[idx]:
            if i % idx == 0:
                return False
    return True


def get_primeNum(PNums):
    for i in range(5, len(PNums), 2):
        if is_prime(i, PNums):
            PNums[i] = True


def print_goldbach(num, PrimeNums):
    for i in range(3, num):
        if PrimeNums[i] and PrimeNums[num - i]:
            # index를 이용하여 두 수가 소수인지 확인하는 것에 O(1)
            print(num, "=", i, "+", num - i)
            return


def solve():
    input = sys.stdin.readline
    TestNum = []
    while True:
        num = int(input())
        if num == 0:
            break
        TestNum.append(num)
    PrimeNums = [False] * (max(TestNum) + 1)
    # index가 소수인 경우 True
    # index 이용 안하고, 소수들의 list를 구하는 방식으로 하면 탐색에 시간이 걸림.
    PrimeNums[2] = True
    PrimeNums[3] = True

    get_primeNum(PrimeNums)
    for T in TestNum:
        print_goldbach(T, PrimeNums)


if __name__ == "__main__":
    solve()
