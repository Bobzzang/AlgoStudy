# https://www.acmicpc.net/problem/9625


def solve():
    N = int(input())
    cnt_A = 1
    cnt_B = 0
    for _ in range(N):
        cnt_A, cnt_B = cnt_B, cnt_A + cnt_B
    print(cnt_A, end=" ")
    print(cnt_B)
    return


if __name__ == "__main__":
    solve()
