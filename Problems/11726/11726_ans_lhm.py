#https://www.acmicpc.net/problem/11726
import sys
input = sys.stdin.readline
N = int(input())
ans = [0,1,2]
for i in range(3,N+1):
    ans.append(ans[i-1]+ans[i-2])

print(ans[N]%10007)Q