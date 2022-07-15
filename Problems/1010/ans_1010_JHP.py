# https://www.acmicpc.net/problem/1010
# 문제 : 다리놓기
# 입력 : 첫 줄 = Test case(T), 둘째~T째줄 = 강 서쪽과 동쪽에 있는 사이트의 개수 (N,M)
# 출력 : 지을 수 있는 다리의 숫자
# 풀이방식 : DP top-down 방식

import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        dp = [[0]*(M+1) for _ in range(N+1)]
        
        if N == M or M <= 1:
            print(1)
        else:
            for i in range(1,N+1):
                for j in range(1,M+1):
                    if i == 1:
                        dp[i][j] = j
                    else:
                        dp[i][j] = dp[i-1][j-1] + dp[i][j-1] # 이부분이 어렵네...
            print(dp[N][M])
        
if __name__ == '__main__':
    solve()