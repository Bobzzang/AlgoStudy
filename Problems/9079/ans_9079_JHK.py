# https://www.acmicpc.net/problem/9079

import sys


def sort_1cnt(arr):
    # Merge sort which '1' bit number increment
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        def compare_1cnt(a, b):
            a_cnt = bin(a).count("1")
            b_cnt = bin(b).count("1")
            if a_cnt < b_cnt:
                return True
            return False

        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if compare_1cnt(left[i], right[j]):
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1

        return res

    return merge(sort_1cnt(arr[: len(arr) // 2]), sort_1cnt(arr[len(arr) // 2 :]))


def coinflip(method):
    # 2**8개의 방법에 대해 어떤 동전이 뒤집히는지를 return
    bitset = format(method, "08b")
    res = 0
    for i in range(8):
        if bitset[i] == "1":
            if i == 0:
                # 1행
                res ^= 1
                res ^= 1 << 1
                res ^= 1 << 2
            elif i == 1:
                # 2행
                res ^= 1 << 3
                res ^= 1 << 4
                res ^= 1 << 5
            elif i == 2:
                # 3행
                res ^= 1 << 6
                res ^= 1 << 7
                res ^= 1 << 8
            elif i == 3:
                # 1열
                res ^= 1
                res ^= 1 << 3
                res ^= 1 << 6
            elif i == 4:
                # 2열
                res ^= 1 << 1
                res ^= 1 << 4
                res ^= 1 << 7
            elif i == 5:
                # 3열
                res ^= 1 << 2
                res ^= 1 << 5
                res ^= 1 << 8
            elif i == 6:
                # 좌상-우하 대각선
                res ^= 1 << 0
                res ^= 1 << 4
                res ^= 1 << 8
            elif i == 7:
                # 우상-좌하 대각선
                res ^= 1 << 2
                res ^= 1 << 4
                res ^= 1 << 6
            i += 1
    return res


def solve():
    input = sys.stdin.readline
    N = int(input())
    T = []
    for _ in range(N):
        Coins = 0
        for _ in range(3):
            c1, c2, c3 = input().split()
            Coins = Coins << 3
            if c1 == "H":
                Coins |= 1 << 2
            if c2 == "H":
                Coins |= 1 << 1
            if c3 == "H":
                Coins |= 1
        T.append(Coins)

    Cases = [x for x in range(2 ** 8)]
    # 뒤집을수 있는 모든 조합은 2**8개이다.
    Cases = sort_1cnt(Cases)
    # 뒤집는 횟수가 작은 순서대로 정렬
    for coin in T:
        is_available = False
        for case in Cases:
            val = coin ^ coinflip(case)

            if val == 511 or val == 0:
                # 모두 H 이거나 모두 T임을 체크
                print(bin(case).count("1"))
                is_available = True
                break
        if is_available == False:
            print(-1)
    return


if __name__ == "__main__":
    solve()
