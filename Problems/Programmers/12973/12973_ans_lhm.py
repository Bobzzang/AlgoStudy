#https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = 0
    a = []


    for i in s:
        if len(a)<1:
            a.append(i)
        else:
            if a[-1]==i:
                a.pop(-1)
            else:
                a.append(i)
    
    if len(a) ==0:
        answer = 1
    else:
        answer = 0


    return answer