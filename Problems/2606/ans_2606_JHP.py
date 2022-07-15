# https://www.acmicpc.net/problem/2606
# (1) 문제 : 바이러스
# (2) 풀이 
# - DFS (깊이우선탐색) 풀이를 통해 깊은 부분을 우선적으로 탐색함
# - Stack으로 Visit 여부를 판정
# - 재귀 함수를 통해 Visit이 완료될때까지 확인
# (3) 느낀점 
# - DFS를 구현하는거 자체는 어렵지 않았음. (Stack을 통한 저장 및 재귀함수)
# - 단, graph를 만드는 것이 좀더 어려웠음.
# - 초기 데이터 input 받는 형태 및 내가 사용하기 용이하도록 숙련 필요

def dfs(array, node, visited):
    global cnt
    visited[node] = True
    
    for i in array[node]:
        if not visited[i]:
            cnt += 1
            dfs(array, i, visited)
    return cnt
    
def solve():
    global cnt
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)] # 1부터 N+1까지의 숫자 범위이기 때문에 N+1만큼 필요 (visit이 Node 1부터 시작)
    
    for i in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)    
    print(graph)
    
    result = 0
    cnt = 0
    visited = [False]*(N+1) # graph와 같은 이유
    
    result = dfs(graph,1,visited)
    print(result)

if __name__ == "__main__":
    solve()
    