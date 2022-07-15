# https://www.acmicpc.net/problem/14916


def solve():
    N = int(input())
    memo = [0] * (max(N, 5) + 1)
    memo[0] = -1
    memo[1] = -1
    memo[2] = 1
    memo[3] = -1
    memo[4] = 2
    memo[5] = 1
    for i in range(6, N + 1):
        minVal = 1000000
        if memo[i - 2] != -1:
            if minVal > memo[i - 2] + 1:
                minVal = memo[i - 2] + 1
        if memo[i - 5] != -1:
            if minVal > memo[i - 5] + 1:
                minVal = memo[i - 5] + 1
        memo[i] = minVal
    print(memo[N])
    return


if __name__ == "__main__":
    solve()
