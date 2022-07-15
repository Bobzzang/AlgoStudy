#https://www.acmicpc.net/problem/1715
import sys
import heapq
input = sys.stdin.readline

N = int(input())
temp = []
ans = 0
for i in range(N):
    heapq.heappush(temp,int(input()))


while len(temp)>1:
    temp1 = heapq.heappop(temp)
    temp2 = heapq.heappop(temp)
    ans += temp1+temp2
    heapq.heappush(temp, temp1+temp2)

print(ans)