# https://www.acmicpc.net/problem/11725

import sys


def solve():

    input = sys.stdin.readline
    N = int(input())
    conn = {}
    for _ in range(N - 1):
        n1, n2 = map(int, input().split())
        if n1 in conn:
            conn[n1] = conn[n1] | {n2}
        else:
            conn[n1] = {n2}
        if n2 in conn:
            conn[n2] = conn[n2] | {n1}
        else:
            conn[n2] = {n1}
    res = {}
    res[1] = 0
    stack = [1]
    # 모든 node는 root가 1번 node인 트리 안에 있으므로,
    # 1번부터 탐색하면 모든 노드를 경유 가능
    while stack:
        node = stack.pop()
        for i in conn[node]:
            if i not in res:
                res[i] = node
                stack.append(i)
                # 깊이우선탐색

    for i in range(2, N + 1):
        print(res[i])
    return


if __name__ == "__main__":
    solve()
