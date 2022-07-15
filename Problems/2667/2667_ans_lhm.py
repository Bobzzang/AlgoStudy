#https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline
N = int(input())

arr = []
danji = []
cnt = 0
for _ in range(N):
    arr.append(list(map(int,input().strip())))


def DFS(x,y):
    global cnt
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        DFS(x+1,y)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x,y-1)
        cnt+=1
        return True
    else:
        return False
danjicnt = 0
for i in range(N):
    for j in range(N):
        if DFS(i,j)==True:
            danji.append(cnt)
            cnt = 0
            danjicnt+=1
danji.sort()
print(danjicnt)
for i in range(danjicnt):
    print(danji[i])
