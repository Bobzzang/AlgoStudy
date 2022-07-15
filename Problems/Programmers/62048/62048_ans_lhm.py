#https://programmers.co.kr/learn/courses/30/lessons/62048
from math import gcd
#문제 이해하는 데 오래걸렸음
#우선 위 문제는 w,h 로 이루어진 직사각형의 대각선을 긋는다고 생각해야됨
#그럼 이제 w,h의 최대 공약수와 연관이 있다는 것을 알 수 있음
#최대 공약수가 1인 경우, 대각선을 지나가는 사각형은 w+h -1 임 ( -1은 첨에 대각선 긋는 순간 겹치기 때문)
#최대 공약수가 g라고 가정해보면 대각선을 지나가는 사각형은 g(w//g+h//g-1) = w+h-g 임
def solution(w,h):
    answer = w*h-(w+h-gcd(w,h))
    return answer

