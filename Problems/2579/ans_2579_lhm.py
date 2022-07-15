#https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*(N+1)
dp = [0]*(N+1)
for i in range(1,N+1):
    arr[i] =int(input())


dp[1]=arr[1]

if N!=1:
    dp[2]=max(arr[1]+arr[2],arr[2])

for i in range(3,N+1):
    dp[i] = max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-2])


print(dp[N])
