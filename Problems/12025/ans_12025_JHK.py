# https://www.acmicpc.net/problem/12025


def solve():
    Password = input()
    K = int(input())
    Res = []
    P = bin(K - 1)[::-1]
    cnt = 0
    for c in Password:
        if c == "1" or c == "2" or c == "6" or c == "7":
            cnt += 1
    if 2 ** cnt < K:
        print(-1)
        return
    cnt = 0
    for c in Password[::-1]:
        if P[cnt] == "0":
            if c == "1":
                Res.append("1")
                cnt += 1
            elif c == "2":
                Res.append("2")
                cnt += 1
            elif c == "6":
                Res.append("1")
                cnt += 1
            elif c == "7":
                Res.append("2")
                cnt += 1
            else:
                Res.append(c)
        elif P[cnt] == "1":
            if c == "1":
                Res.append("6")
                cnt += 1
            elif c == "2":
                Res.append("7")
                cnt += 1
            elif c == "6":
                Res.append("6")
                cnt += 1
            elif c == "7":
                Res.append("7")
                cnt += 1
            else:
                Res.append(c)
        else:
            if c == "1":
                Res.append("1")
            elif c == "2":
                Res.append("2")
            elif c == "6":
                Res.append("1")
            elif c == "7":
                Res.append("2")
            else:
                Res.append(c)
    print("".join(list(reversed(Res))))
    return


if __name__ == "__main__":
    solve()
