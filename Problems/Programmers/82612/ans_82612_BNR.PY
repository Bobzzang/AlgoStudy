'''
https://programmers.co.kr/learn/courses/30/lessons/82612#

'''
def solution(price, money, count):
    answer = -1

    for cnt in range(1,count+1):
        money -= cnt*price
    
    if money >0:
        return 0
    else:
        answer = abs(money)
    return answer