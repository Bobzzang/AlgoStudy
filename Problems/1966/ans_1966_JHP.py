# https://www.acmicpc.net/problem/1966
# 문제 : 프린터큐
# 입력 : 첫줄 = TC 수, 
#      : TC 첫줄 = [문서 개수 N, 궁금한 문서가 현재 Queue에 몇 번째인지 M]
#      : TC 둘째줄 = N개 문서의 중요도 
# 출력 : 각 TC별 문서가 몇번째 출력 되는지 확인

import sys

def solve():
    input = sys.stdin.readline
    TC = int(input())
    
    for _ in range(TC):
        N,M = map(int,input().split())
        input_doc = list(map(int,input().split()))
        result = [0]*N
        result[M] = 'True'
        cnt = 0
        
        while True:
            if input_doc[0] == max(input_doc):
                cnt += 1
                if result[0] == 'True':
                    print(cnt)
                    break
                else:
                    input_doc.pop(0)
                    result.pop(0)
            else:
                input_doc.append(input_doc.pop(0))
                result.append(result.pop(0))    

if __name__ == '__main__':
    solve()