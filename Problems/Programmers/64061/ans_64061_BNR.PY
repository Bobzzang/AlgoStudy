'''
https://programmers.co.kr/learn/courses/30/lessons/64061

'''
def solution(board, moves):
    cnt = 0
    basket = []
    
    for j in moves:
        for i in range(len(board[1])):
            if board[i][j-1] == 0:
                continue
            else:
                if len(basket)==0:
                    basket.append(board[i][j-1])
                elif basket[-1]==board[i][j-1]:
                    basket.pop()
                    cnt += 2
                else:                
                    basket.append(board[i][j-1])
                board[i][j-1] = 0
                break 
    return cnt