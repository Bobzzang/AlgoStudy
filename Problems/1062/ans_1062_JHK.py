# https://www.acmicpc.net/problem/1062

import sys
import itertools


def make_wordmask(K):
    if K < 5:
        return [0]
    defaultChar = "antatica"
    defMask = 0
    for c in defaultChar:
        defMask |= 1 << (ord(c) - ord("a"))

    if K == 5:
        return [defMask]

    refchar = ""
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in defaultChar:
            refchar += chr(i)

    combSet = list(itertools.combinations(refchar, K - 5))
    res = []
    for combStr in combSet:
        WordMask = 0
        for c in combStr:
            WordMask |= 1 << (ord(c) - ord("a"))
        res.append(WordMask + defMask)
    return res


def check_word_valid(word, mask):
    if word & mask == word:
        return 1
    return 0


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    WordSet = []
    for _ in range(N):
        tempWord = input().rstrip()
        tempRes = 0
        for c in tempWord:
            tempRes |= 1 << (ord(c) - ord("a"))
        WordSet.append(tempRes)
    WordMask = make_wordmask(K)
    MaxCnt = 0
    for mask in WordMask:
        cnt = 0
        for word in WordSet:
            cnt += check_word_valid(word, mask)
        if cnt > MaxCnt:
            MaxCnt = cnt
    print(MaxCnt)
    return


if __name__ == "__main__":
    solve()
