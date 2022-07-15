# https://www.acmicpc.net/problem/1124


def solve():
    A, B = map(int, input().split())
    # max_limit = int(B**0.5) + 1
    max_limit = B + 1
    PrimeNums = [True] * (max_limit + 1)
    PrimeNums[0] = False
    PrimeNums[1] = False
    i = 2
    while i <= max_limit:
        if PrimeNums[i]:
            j = i + i
            while j <= max_limit:
                PrimeNums[j] = False
                j += i
        i += 1
    underprimeCnt = 0
    for i in range(A, B + 1):
        if PrimeNums[i] == False:
            # 소수는 unerprime이 될 수 없음.
            p = i
            j = 2
            cnt = 0
            while j <= i:
                if PrimeNums[j]:
                    if i % j == 0:
                        i //= j
                        cnt += 1
                        continue
                j += 1
            if PrimeNums[cnt]:
                underprimeCnt += 1
    print(underprimeCnt)
    return


if __name__ == "__main__":
    solve()
