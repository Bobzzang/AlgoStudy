#https://www.acmicpc.net/problem/1789

N = int(input())

#ans_buff = []
minchk = 0
i =1
while i<=N:
    N = N-i
    minchk = i
    i+=1
    if minchk == i:
        i+=1

    #print("i:",i)
    #print("minchk:",minchk)
    #print("N:",N)
print(i-1)