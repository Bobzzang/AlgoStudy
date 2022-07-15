'''
1. DFS(Depth-Frist Search) 개요
  - DFS는 "깊이우선탐색"이라고 하며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
  - 주로 Stack 자료구조 or 재귀함수를 이용
  - 동작 과정
    (1) 탐색 시작 노드를 Stack에 삽입하고 방문 처리함. (Flag나 True/False로 표기)
    (2) Stack의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면, 그 노드를 스택에 넣고 방문 처리함.
    (3) (2)의 과정이 수행되지 않을때까지 반복
  - DFS는 주로 번호가 낮은 노드를 먼저 방문 처리함
    : 가장 깊은 오소까지 모두 확인하는 방식이기 떄문에 재귀함수로 구현 가능 
'''

# DFS 함수 정의
def dfs(array, node, visited):
    visited[node] = True
    print(node, end=' ')
    
    for i in array[node]:
        if not visited[i]:
            dfs(array, i, visited)
    
def solve():
    N = int(input())
    input_arr = [list(map(int,input().split())) for _ in range(N)]
    print(input_arr)
    
    visited = [False]*N
    
    dfs(input_arr,1,visited)

if __name__ == "__main__":
    solve()
    