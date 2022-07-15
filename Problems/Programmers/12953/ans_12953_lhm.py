#https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    max_val = max(arr)
    check = False
    c = 1
    result = max_val
    answer = 1
    while True:
        for i in arr:
            if result%i==0:
                check = True
            else:
                check = False
                c+=1
                result = c*max_val
                break
        if check == True:
            return result
        
    return answer