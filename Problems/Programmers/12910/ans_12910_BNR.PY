'''
https://programmers.co.kr/learn/courses/30/lessons/12910

'''
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor==0:
            answer.append(num)
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer