#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def DFS(i,result):
        if i == n:
            if result == target:
                nonlocal answer
                answer +=1
            return
        else:
            DFS(i+1, result+numbers[i])
            DFS(i+1, result-numbers[i])
    
    DFS(0,0)
    return answer