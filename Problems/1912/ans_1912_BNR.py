'''
https://www.acmicpc.net/problem/1912

'''
import sys

def solve():
    input = sys.stdin.readline
    N= int(input())
    Numlist = list(map(int, input().split()))

    dp = [-1001]*N
    dp[0] = Numlist[0]
    for i in range(1,len(Numlist)):
        dp[i] = max(dp[i-1]+Numlist[i], Numlist[i])

    print(max(dp))

if __name__ == "__main__":
    solve()    