# https://www.acmicpc.net/problem/11066


def divMin(data, dic, st, ed):
    if (st, ed) in dic:
        return dic[st, ed]
    l = ed - st
    res = []
    sumRaw = sum(data[st : ed + 1])
    minval = 500 * 10000
    for i in range(l):
        mid = st + i
        val1 = divMin(data, dic, st, mid)
        val2 = divMin(data, dic, mid + 1, ed)
        if val1 + val2 < minval:
            minval = val1 + val2
    dic[st, ed] = minval + sumRaw
    return dic[st, ed]


def calcMin(data):
    dic = {}
    for i in range(len(data)):
        dic[i, i] = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            divMin(data, dic, i, j)
    print(dic[0, len(data) - 1])


def solve():
    T = int(input())
    TC = []
    for _ in range(T):
        input()
        TC.append(list(map(int, input().split())))

    for t in TC:
        calcMin(t)
    return


if __name__ == "__main__":
    solve()
