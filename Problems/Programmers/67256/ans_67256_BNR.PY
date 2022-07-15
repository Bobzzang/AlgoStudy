'''
https://programmers.co.kr/learn/courses/30/lessons/67256

'''
def solution(numbers, hand):
    answer = ''
    key = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

    Le_dist = 3     #세로
    Ri_dist = 3
    Le_index = 0    #가로
    Ri_index = 0
    
    for num in numbers:
        for idx, key_list in enumerate(key):
            if num in key_list:
                if num == key_list[0]:
                    answer = answer+'L'
                    Le_dist = idx
                    Le_index = 0
                    continue
                if num == key_list[2]:
                    answer = answer+'R'
                    Ri_dist = idx
                    Ri_index = 0
                    continue
                
                # print(num, Le_dist, Ri_dist)
                if abs(Le_dist - idx)+abs(Le_index-1) < abs(Ri_dist - idx)+abs(Ri_index-1):
                    answer = answer+'L'
                    Le_dist = idx
                    Le_index = 1
                elif abs(Ri_dist - idx)+abs(Ri_index-1) < abs(Le_dist - idx)+abs(Le_index-1):
                    answer = answer+'R'
                    Ri_dist = idx
                    Ri_index = 1
                else:
                    if hand == 'left':
                        answer = answer+'L'
                        Le_dist = idx
                        Le_index = 1
                    elif hand == 'right':
                        answer = answer+'R'
                        Ri_dist = idx
                        Ri_index = 1
            
    return answer