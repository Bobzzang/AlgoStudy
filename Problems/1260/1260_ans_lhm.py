#https://www.acmicpc.net/problem/1260
import sys
input = sys.stdin.readline
N, M, V = list(map(int,input().split()))

matrix = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = list(map(int,input().split()))
    matrix[a][b] =1
    matrix[b][a] =1



def DFS(start,visited):
    visited += [start]
    for i in range(len(matrix[start])):
        if matrix[start][i]==1 and (i not in visited):
            DFS(i, visited)
    return visited

def BFS(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for i in range(len(matrix[n])):
            if matrix[n][i] ==1 and (i not in visited):
                visited.append(i)
                queue.append(i)
    return visited

print(*DFS(V,[]))
print(*BFS(V))