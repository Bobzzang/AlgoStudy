#https://www.acmicpc.net/problem/1436
import sys
input = sys.stdin.readline
chk = 666
cnt = 0
N = int(input())
while True:
    if '666' in str(chk):
        cnt +=1
    if cnt==N:
        print(chk)
        break
    chk+=1

