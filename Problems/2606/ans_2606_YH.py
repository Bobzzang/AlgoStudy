#https://www.acmicpc.net/problem/2606
from collections import deque

# bfs로 풀기
def bfs(node, graph, visited):
    queue = deque([node])
    visited[node] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt+=1
    return cnt

# Stack dfs로 풀기
def dfs(node, graph, visited):
    stack = deque([node])
    cnt = 0

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            stack.extend(graph[v])
            cnt+=1
            print(v, end=" ")
    return (cnt-1)

# Recursion dfs로 풀기
def dfs_Recursion(node, graph, visited):
    global infectNum
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs_Recursion(i, graph, visited)
            infectNum+=1
    return infectNum

def solve():
    n = int(input())
    m = int(input())
    graph = {}
    global infectNum
    infectNum = 0
    for _ in range(m):
        a,b =map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph: # For bidirection
            graph[b] = [a]
        else:
            graph[b].append(a)
    # print(graph)
    visited = [False]*(n+1)
    
    # bfs로 풀기
    print(bfs(1, graph, visited))
    # stack bfs로 풀기 
    print(dfs(1, graph, visited))
    # recursion bfs로 풀기
    print(dfs_Recursion(1, graph, visited))

    return

if __name__ == "__main__":
    solve()