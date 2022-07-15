# https://www.acmicpc.net/problem/11866
# 문제 : 요세푸스 문제
# 입력 : 첫번째 = N, K (K번째)

import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    list_N = []
    result = []
    
    for i in range(1,N+1):
        list_N.append(i)

    while list_N:
        for i in range(K-1): # K번째 숫자
            list_N.append(list_N.pop(0)) # K번째 전까지는 뒤로 붙이기
        result.append(str(list_N.pop(0)))     # list_N의 첫번째 숫자가 K번째이므로 저장

    print(f"<{', '.join(result)}>") # f.{}을 통해서 result값 표출

if __name__ == "__main__":
    solve()