# https://www.acmicpc.net/problem/10866
# Dequeue(덱) 구현

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class deque:
    # 초기화
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # (1) push_front 구현
    def push_front(self,data): 
        new_node = Node(data) # data 추가
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node # push_front이기 때문에 맨앞 front와 연결
            new_node.next = self.head # 추가 deque 연결 부분
            self.head = new_node
        self.size += 1
    # (2) push_back 구현
    def push_back(self,data):
        new_node = Node(data) # data 추가
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # push_back이기 때문에 맨마지막 tail과 연결
            new_node.prev = self.tail # 추가 deque 연결 부분
            self.tail = new_node
        self.size += 1
    # (3) pop_back 구현
    def pop_front(self):
        front_data = None
        if self.isEmpty() == True:
            front_data = -1
        else:
            front_data = self.head.data
            self.head = self.head.next # 맨 앞에 값이 뽑히고, 다음 값으로 작성
            self.size -= 1
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return front_data
    # (4) pop_back 구현
    def pop_back(self):
        back_data = None
        if self.isEmpty() == True:
            back_data = -1
        else:
            back_data = self.tail.data
            self.tail = self.tail.prev # 맨 끝 값이 뽑히고, 이전 값을 마지막으로 설정
            self.size -= 1
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None
        return back_data
    # (5) size 구현
    def que_size(self):
        return self.size
    # (6) Empty 여부 판단
    def isEmpty(self):
        is_empty = False
        if self.head == None:
            is_empty = True
        return is_empty
    # (7) Front 값 출력 구현
    def front(self):
        if self.isEmpty() == True:
            print('-1')
        else:
            print(self.head.data)
    # (8) back 값 출력 구현
    def back(self):
        if self.isEmpty() == True:
            print('-1')
        else:
            print(self.tail.data)

def solve():
    input = sys.stdin.readline
    N = int(input())
    Deq = deque()
    for _  in range(N):
        req = input().split()
        if req[0] == 'pop_front':
            print(Deq.pop_front())
        elif req[0] == 'pop_back':
            print(Deq.pop_back())
        elif req[0] == 'front':
            Deq.front()
        elif req[0] == 'back':
            Deq.back()
        elif req[0] == 'empty':
            if Deq.size == 0:
                print('1')
            else:
                print('0')
        elif req[0] == 'size':
            print(Deq.size)
        elif req[0] == 'push_front':
            Deq.push_front(int(req[1]))
        elif req[0] == 'push_back':
            Deq.push_back(int(req[1]))

if __name__ == '__main__':
    solve() 