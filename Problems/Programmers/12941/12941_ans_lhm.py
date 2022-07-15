#https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]

    return answer