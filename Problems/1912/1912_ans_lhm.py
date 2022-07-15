#acmicpc.net/problem/1912
import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N)
arr = []
arr = list(map(int,(input().split())))
dp[0] = arr[0]
for i in range(N-1):
    dp[i+1] = max(dp[i]+arr[i+1],arr[i+1])

print(max(dp))

