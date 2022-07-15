# https://www.acmicpc.net/problem/9012
# 문제 : 입력 괄호 문자열이 올바른 괄호 문자열인지 아닌지를 판단하는 프로그램 작성 (VPS, Valid Parenthesis String)
# 입력 : 첫째줄 = Test case 숫자 T, 둘째줄 = Test할 괄호 열
# 출력 : Yes / No 출력

import sys

def solve():
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        input_str = list(input().rstrip())
        stack = []
        for i in range(len(input_str)):
            if input_str[i] == '(':
                stack.append(input_str[i])
            elif input_str[i] == ')' and'(' not in stack:
                stack.append(input_str[i])
            else:
                stack.pop()
        if len(stack) == 0: 
            print("YES")
        else: 
            print("NO")
    
if __name__ == "__main__":
    solve()