# https://www.acmicpc.net/problem/2565 
# 문제 : 전깃줄
# 입력 : 첫째 줄 = 전깃줄 숫자 N, 둘째줄 ~ N째줄 = A,B 위치
# 출력 : 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄 최소 개수
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    dp = [1]*N    # 시작이 1부터이기 때문에 Default값도 1로 설정

    # input A,B
    pole = [0]*N
    for i in range(N):
        pole[i] = list(map(int,input().split()))
    # pole = [list(map(int,input().split())) for _ in range(N)]
    pole.sort(key=lambda x:x[0]) # A를 기준으로 정렬
    
    # dp 풀이
    for i in range(N):
        for j in range(i):
            if pole[i][1] > pole[j][1]:
                dp[i] = max(dp[i], dp[j]+1)    
    print(N-max(dp))

if __name__ == "__main__":
    solve()