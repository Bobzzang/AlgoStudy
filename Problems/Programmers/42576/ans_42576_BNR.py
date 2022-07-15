'''
https://programmers.co.kr/learn/courses/30/lessons/42576
'''
def solution(participant, completion):
    #for name in participant:
        #solution 1 시간초과
        # if name in completion:        
        #      completion.remove(name)
        # else:
        #     return name
        
        #solution 2 시간초과
        #for i in range(len(completion)):
        #    if name == completion[i]:
        #        completion.remove(name)
        #        break
        #    if i == len(completion)-1:
        #        return name
        
    participant.sort()
    completion.sort()

    for i in range(len(participant)-1):
        if participant[i] == completion[i]:
            continue
        else:
            return participant[i]
    return participant[-1]