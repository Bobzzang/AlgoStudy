'''
https://programmers.co.kr/learn/courses/30/lessons/42748
'''

def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        ref_array = array[i-1:j]
        ref_array.sort()
        answer.append(ref_array[k-1])
    return answer