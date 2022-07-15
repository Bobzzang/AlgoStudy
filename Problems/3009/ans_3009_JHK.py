# https://www.acmicpc.net/problem/3009


def solve():
    x = {}
    y = {}
    a, b = map(int, input().split())
    if a not in x:
        x[a] = 1
    else:
        x[a] += 1
    if b not in y:
        y[b] = 1
    else:
        y[b] += 1
    a, b = map(int, input().split())
    if a not in x:
        x[a] = 1
    else:
        x[a] += 1
    if b not in y:
        y[b] = 1
    else:
        y[b] += 1
    a, b = map(int, input().split())
    if a not in x:
        x[a] = 1
    else:
        x[a] += 1
    if b not in y:
        y[b] = 1
    else:
        y[b] += 1
    for p in x:
        if x[p] == 1:
            print(p, end=" ")
            break
    for q in y:
        if y[q] == 1:
            print(q)
            break
    return


if __name__ == "__main__":
    solve()
