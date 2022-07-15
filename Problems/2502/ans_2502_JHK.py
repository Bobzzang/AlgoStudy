# https://www.acmicpc.net/problem/2502

# An = An-1 + An-2
#    = Pn-2*A2 + Pn-3*A1  (P: 1, 1, 2, 3 으로 시작하는 피보나치 수열)


def get_init_dduk(K, a, b):
    # K = a*D2 + b*D1
    D1 = 1
    while True:
        if (K - b * D1) % a == 0:
            D2 = (K - b * D1) // a
            break
        D1 += 1
    return D2, D1


def solve():
    D, K = map(int, input().split())
    P = [1, 1]
    i = 1
    while i < D:
        temp = P[-1] + P[-2]
        P.append(temp)
        i += 1
    D2, D1 = get_init_dduk(K, P[D - 2], P[D - 3])
    print(D1)
    print(D2)

    return


if __name__ == "__main__":
    solve()
