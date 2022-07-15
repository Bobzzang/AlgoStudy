#https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline

N = int(input())
arr_rope = []
ans = []
for i in range(N):
    arr_rope.append(int(input()))

arr_rope.sort(reverse=True)

for i in range(len(arr_rope)):
    ans.append(arr_rope[i]*(i+1))
print(max(ans))
