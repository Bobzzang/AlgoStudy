#https://www.acmicpc.net/problem/11052
# dp[i] : i개의 카드를 구매하는 최대 가격
# card[k] : k개의 카드팩이 들어 있는 가격
# card[1]+dp[i-1]
# card[2]+dp[i-2]
# ...
# dp[i] = card[k]+dp[i-k]
import sys
input = sys.stdin.readline

N = int(input())
card = []

card = list(map(int,input().split()))
card = [0]+card
dp = [0]*(N+1)

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i],card[k]+dp[i-k])
        #print(dp)

print(dp[N])