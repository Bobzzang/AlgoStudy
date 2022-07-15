# https://www.acmicpc.net/problem/2164
# 문제 : N개의 카드 중 마지막에 남는 카드의 숫자 찾기
# 입력 : N개의 카드 숫자
# 출력 : 마지막에 남는 카드 찾기
# --------------------------------------------------------------
# deque(double-end queue)를 사용 해야 시간초과 없이 해결 가능
# deque는 append와 pop에 대해 O(1) 시간 복잡도를 가지고 있음
# List의 append와 pop은 O(n) 시간 복잡도를 지니기 때문에, deque가 보다 효과적임
# https://blog.naver.com/dsz08082/222559458327

import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    queue = deque()

    for i in range(1, N+1):
        queue.append(i)

    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[-1])

if __name__ == '__main__':
    solve()

''' 시간 초과 
def solve_failed():
    input = sys.stdin.readline
    N = int(input())
    queue = []
    
    for i in range(1,N+1):
        queue.append(i)
    
    while len(queue) > 1:
        queue.remove(queue[0])
        temp = queue[0]
        queue.append(temp)
        queue.remove(queue[0])
    print(queue[-1])
'''

