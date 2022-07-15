'''
https://www.acmicpc.net/problem/10816

'''
import sys

def bs_down(N_list, num):
    left = 0
    right = len(N_list)-1

    while left<=right:
        if left >right:
            return 0
        mid = (left+right)//2
        if N_list[mid]>=num:
            right = mid-1
        elif N_list[mid]<num:
            left = mid+1
    return left
def bs_up(N_list, num):
    left = 0
    right = len(N_list)-1

    while left<=right:
        if left >right:
            return 0
        mid = (left+right)//2
        if N_list[mid]>num:
            right = mid-1
        elif N_list[mid]<=num:
            left = mid+1
    return left
def solve():
    input = sys.stdin.readline
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    
    N_list.sort()

    for tar in M_list:
        print(bs_up(N_list,tar)-bs_down(N_list,tar), end = ' ')

if __name__ == "__main__":
    solve()    