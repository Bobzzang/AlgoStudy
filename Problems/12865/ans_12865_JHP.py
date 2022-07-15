# https://www.acmicpc.net/problem/12865
# 평범한 배낭 : 가치있는 가방 만들기
# 입력 : 첫째줄 = 물품의 수 N, 가방 허용 무게 K
#        둘~N째줄 = 무게 W, 가치 V
# 출력 : 물건 가치합
'''
참고 : https://blog.naver.com/swanyte/222408717583
Knapsack Problem(냅섹) 문제에 대해 좀더 공부 필요
'''

import sys

def solve():
    input = sys.stdin.readline
    N, K = list(map(int,input().split()))
    bag_info = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,K+1):
            if j < bag_info[i-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                # 아래 점화식을 찾는게 어렵네요...
                dp[i][j] = max(dp[i-1][j], bag_info[i-1][1]+dp[i-1][j-bag_info[i-1][0]])
    print(dp[N][K])

if __name__ == '__main__':
    solve()