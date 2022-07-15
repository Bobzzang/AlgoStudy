'''
https://programmers.co.kr/learn/courses/30/lessons/68644

'''
def solution(numbers):
    sum_list=[]
    for i in range (len(numbers)):
        for j in range(i+1, len(numbers)):
            sumNum = numbers[i]+numbers[j]
            if sumNum in sum_list:
                continue
            sum_list.append(numbers[i]+numbers[j])
    sum_list.sort()
    return sum_list