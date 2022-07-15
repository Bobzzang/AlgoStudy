'''
https://www.acmicpc.net/problem/1269

'''
import sys

def solve_1():
    input = sys.stdin.readline

    A, B = map(int, input().split())
    A_set = set(map(int, input().split()))
    B_set = set(map(int, input().split()))
    print(len(A_set-B_set)+len(B_set-A_set))

def solve_2():  #시간초과
    input = sys.stdin.readline

    A, B = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    if A<B:
        for i in B_list:
            if i in A_list:
                B_list.remove(i)
                A_list.remove(i)
            
    else:
        for i in A_list:
            if i in B_list:
                B_list.remove(i)
                A_list.remove(i)
    print(len(A_list)+len(B_list))

if __name__ == "__main__":
    solve_1()    