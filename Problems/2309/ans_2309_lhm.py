#https://www.acmicpc.net/problem/2309
import sys
from itertools import combinations
input = sys.stdin.readline
temp1 = []
ans = []
for _ in range(9):
    temp1.append(int(input()))

temp2 = list(combinations(temp1,7))

for i in range(len(temp2)):
    if sum(temp2[i]) == 100:
        ans = temp2[i]
        break
ans = list(ans)
ans.sort()
for i in ans:
    print(i)