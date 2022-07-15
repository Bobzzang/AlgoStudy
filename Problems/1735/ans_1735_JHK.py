# https://www.acmicpc.net/problem/1735


def GCD(A, B):
    # A should be bigger than B
    if B == 0:
        return A
    return GCD(B, A % B)


def solve():
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    A = P[0] * Q[1] + P[1] * Q[0]
    B = P[1] * Q[1]
    if A > B:
        D = GCD(A, B)
    else:
        D = GCD(B, A)

    print(A // D, B // D)
    return


if __name__ == "__main__":
    solve()
