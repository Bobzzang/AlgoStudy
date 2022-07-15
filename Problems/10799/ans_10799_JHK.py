# https://www.acmicpc.net/problem/10799


def solve():
    s = input()
    idx = 0
    depth = 0
    ret = 0
    while len(s) > idx:
        if s[idx] == "(" and s[idx + 1] == ")":
            ret += depth
            idx += 2
            continue
        if s[idx] == "(":
            depth += 1
        else:
            depth -= 1
            ret += 1
        idx += 1
    print(ret)
    return


if __name__ == "__main__":
    solve()
