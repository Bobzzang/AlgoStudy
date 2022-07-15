# https://www.acmicpc.net/problem/11659
# 문제 : 구간 합 구하기4
# 입력 : 첫째줄 = 숫자 갯수 N, Test 횟수 M, 둘째줄 = N개의 숫자, 셋째줄~M줄 = i,j번째
# 출력 : i~j번째까지 합 (M번 수행)

import sys

def solve():
    input = sys.stdin.readline
    N, M = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    sum = [0]*N
    ans = []
    
    for idx in range(N):
        if idx == 0:
            sum[idx] = nums[idx]
        else:
            sum[idx] = sum[idx-1] + nums[idx] # for가 아닌 미리 계산 수행
    
    for _ in range(M):        
        i,j = map(int,input().split())
        if i == 1:
            ans.append(sum[j-1])
        else:
            ans.append(sum[j-1] - sum[i-2])  # index와 i,j번째 matching 필요

    for val in ans:
        print(val)
    
if __name__ == "__main__":
    solve()
    
''' 시간초과
def solve_failed():
    
    input = sys.stdin.readline
    N, M = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    TC = []
    
    for _ in range(M):
        TC.append(list(map(int,input().split())))
    
    for idx in TC:
        sum = 0
        i = idx[0]
        j = idx[1]
        for k in range(i-1,j):
            sum += nums[k]
        print(sum)
'''