# https://www.acmicpc.net/problem/14490


def solve():
    a, b = map(int, input().split(":"))
    p = a
    q = b
    is_swapped = False
    if p < q:
        is_swapped = True
        p, q = q, p

    while q != 0:
        p, q = q, p % q
    print(a // p, end=":")
    print(b // p)

    return


if __name__ == "__main__":
    solve()
