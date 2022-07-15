'''
https://www.acmicpc.net/problem/10773

스택
LIFO(Last In First Out)

'''
import sys

def solve():
    K = int(sys.stdin.readline())
    input_list=[]
    stack_list=[]
    for _ in range(K):
        input_list.append(int(sys.stdin.readline()))
        
    for i in input_list:
        if i != 0:
            stack_list.append(i)
        else:
            del stack_list[-1]
    print(sum(stack_list))

if __name__ == "__main__":
    solve()