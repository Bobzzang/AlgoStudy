#https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
dp = [0]*(N+1)
for _ in range(N):
    a, b  = map(int,input().split())
    T.append(a)
    P.append(b)

for i in range(N-1,-1,-1):
    if i+T[i]>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[T[i]+i])
print(max(dp))