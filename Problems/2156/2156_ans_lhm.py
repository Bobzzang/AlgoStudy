#https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [0]*(N+1)
for _ in range(N):
    arr.append(int(input()))
arr = [0] + arr
if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1]+arr[2])

else:
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2]

    for n in range(3, N+1):
        dp[n] = max(arr[n]+arr[n-1]+dp[n-3], arr[n]+dp[n-2], dp[n-1])
        #print(dp)
    print(dp[-1])


