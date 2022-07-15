#https://www.acmicpc.net/problem/2178
N, M = map(int,input().split())
matrix = []
pos_queue = [(0,0)]
cnt_queue = [1]
end_pos = (N-1, M-1)


for i in range(N):
    matrix+=[list(map(int,input()))]

def is_can_go(x,y):
    if (0<=x<N and 0<=y<M):
        if matrix[x][y] == 1:
            return True
        else:
            return False
    else:
        return False


while len(pos_queue)!=0:
    pos = pos_queue.pop(0)
    cnt = cnt_queue.pop(0)
    x = pos[0]
    y = pos[1]

    if pos == end_pos:
        print(cnt)
        break
    elif matrix[x][y] == 0:
        continue
    matrix[x][y] = 0

    if(is_can_go(x+1,y)):
        pos_queue.append((x+1,y))
        cnt_queue.append(cnt+1)
    if(is_can_go(x-1,y)):
        pos_queue.append((x-1,y))
        cnt_queue.append(cnt+1)       
    if(is_can_go(x,y+1)):
        pos_queue.append((x,y+1))
        cnt_queue.append(cnt+1)
    if(is_can_go(x,y-1)):
        pos_queue.append((x,y-1))
        cnt_queue.append(cnt+1)                  
