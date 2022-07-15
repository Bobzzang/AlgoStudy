# https://www.acmicpc.net/problem/20921

# K = 0 인 경우 : 1 2 3 ... N
# K = N*(N-1)/2 인 경우 : N N-1 N-2 ... 1

# K < N 인 경우 중 하나 : N 1 2 3 ... N-1
# 위를 이용하면, K >= N인 경우
# 1. N을 맨 앞에 둬서 N-1개의 그렇고그런사이를 확보
# 2. 1 ~ N-1 중에서 K-(N-1)개를 확보해야 함.
# 3. N-1 = N', K-(N-1) = K' 이라 하면 1부터 반복 가능


def solve():
    N, K = map(int, input().split())
    res = []
    while True:
        if K >= N:
            res.append(N)
            K -= N - 1
            N -= 1
        else:
            Temp = K + 1
            res.append(Temp)
            for i in range(1, N + 1):
                if i != Temp:
                    res.append(i)
            break
    print(*res)
    return


if __name__ == "__main__":
    solve()
