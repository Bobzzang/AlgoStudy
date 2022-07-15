#https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []        
    s = s[2:-2].split('},{')
    new_s =[]
    for x in s:
        new_s.append(x.split(','))
    new_s.sort(key=len)
    for x in new_s:
        for i in range(len(x)):
            if not int(x[i]) in answer:
                answer.append(int(x[i]))
    print(answer)
    return answer

if __name__ =="__main__":
   print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) 