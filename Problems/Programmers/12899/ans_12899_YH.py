#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = []
    while n:
        t = n % 3
        if not t:
            t = 3
            n -= 1
        answer.append(str(t))
        n //= 3
    # print(answer[::-1])
    for i,x in enumerate(answer):
        if x == '3':
            answer[i] = '4'
    return ''.join(answer[::-1])

if __name__ == "__main__":
    print(solution(100))