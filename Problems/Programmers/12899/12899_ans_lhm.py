#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    arr = '124'
    answer = ''
    num = n
    while True:
        if num > 3:
            a= num%3
            num = num//3
            if a ==0:
                num = num -1
                a = 3
            answer += arr[a-1]
        else:
            answer += arr[num-1]
            break

    return answer[::-1]