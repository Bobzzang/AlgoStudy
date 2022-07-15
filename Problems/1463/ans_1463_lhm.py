#https://www.acmicpc.net/problem/1463
#메모이제이션 문제
#풀이 과정의 모든 수를 배열에 넣음으로써 실행 시간을 단축할 수 있음
#아래의 문제의 경우 숫자를 가장빠르게 줄이려면 10에서 1이 아니라
#1에서 10을 어떻게 하면 빠르게 바꿀 수 있을 지를 고려

import sys
input = sys.stdin.readline

N = int(input())
arr = (N+1)*[0]

for i in range(2,N+1):
    arr[i] = arr[i-1]+1 #1을 빼는 것은 카운터 누적
    if i % 3 == 0:
        arr[i] = min(arr[i],arr[i//3]+1) #3으로 나누는게 이득일지 아닐지
    if i % 2 == 0:
        arr[i] = min(arr[i],arr[i//2]+1) #2로 나누는게 이득일지 아닐지
    #print("i:",i)
    #print('arr:',arr)
print(arr[N])        