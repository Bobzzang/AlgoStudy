#https://programmers.co.kr/learn/courses/30/lessons/42586

#
def solution(progresses, speeds):
    answer = []
    rem = [(100-x) for x in progresses]
    temp = []
    for i in range(len(speeds)):
        date = rem[i]//speeds[i]
        if rem[i]%speeds[i] !=0:
            date +=1
        temp.append(date)
    # cnt, std, i = 1,0,0
    # while True:
    #     i+=1
    #     if i == len(temp):
    #         answer.append(cnt)
    #         break
    #     if temp[std] >= temp[i]:
    #         cnt+=1
    #         continue
    #     else:
    #         std = i
    #     answer.append(cnt)
    #     cnt = 1
# Solution2 풀이 적용하여 While문에 대해 대체한 경우
    for x in temp:
        if len(answer) == 0 or answer[-1][0] < x:
            answer.append([x,1])
        else:
            answer[-1][1]+=1

    return print([x[1] for x in answer])

# 다른 사람 풀이..
def solution2(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds): # zip 함수 - 위의 Line 6~12 대체
        delivery = -(p-100)//s # 나누기 및 올림에 대한 1줄 표현 - 위의 Line 8~11 대체
        if len(answer) == 0 or (answer[-1][0] < delivery):
            answer.append([delivery, 1])
        else:
            answer[-1][1]+=1

    return [x[1] for x in answer]



if __name__ =="__main__":
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])