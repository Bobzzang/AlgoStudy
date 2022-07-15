'''
https://www.acmicpc.net/problem/11726

'''
import sys

def solve():
    N = int(sys.stdin.readline())
    dp = [0]*1001

    dp[1] = 1
    dp[2] = 2
    if N>=3:
        for i in range(3, N+1):
            dp[i] = dp[i-1]+dp[i-2]
    answer = dp[N]%10007
    print(answer)

if __name__ == "__main__":
    solve()