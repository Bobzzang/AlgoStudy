#https://www.acmicpc.net/problem/10866
import sys
input = sys.stdin.readline

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def Push_front(self,data):
        self.size +=1
        NewNode = Node(data)
        if self.head == None:
            self.head = self.tail = NewNode
            return 
        # NewNode.prev = self.head
        # NewNode.next = self.head.next
        self.head.prev = NewNode
        NewNode.next = self.head
        self.head = NewNode
    def Push_back(self,data):
        self.size +=1
        NewNode = Node(data)
        if self.head == None:
            self.head = self.tail = NewNode
            return  
        # NewNode.prev = self.tail.prev
        # NewNode.next = self.tail
        self.tail.next = NewNode
        NewNode.prev = self.tail
        self.tail = NewNode
    def Pop_front(self):
        if not self.head:
            return -1
        self.size-=1
        temp = self.head.data
        self.head = self.head.next
        if not self.head : 
            self.tail = None
        else: 
            self.head.prev = None
        return temp
    def Pop_back(self):
        if not self.head:
            return -1
        self.size-=1
        temp = self.tail.data
        self.tail = self.tail.prev
        if not self.tail : 
            self.head = None
        else:
            self.tail.next = None
        return temp
    def is_empty(self):
        return +(not self.head)
    def qfront(self):
        return self.head.data if self.head else -1
    def qback(self):
        return self.tail.data if self.tail else -1

def solve():
    N = int(input())
    deque = Deque()
    for _ in range(N):
        cmd = list(input().split())
        if cmd[0] == "push_front":
            deque.Push_front(cmd[1])
        elif cmd[0] == "push_back":
            deque.Push_back(cmd[1])
        elif cmd[0] == "front":
            print(deque.qfront())
        elif cmd[0] == "back":
            print(deque.qback())
        elif cmd[0] == "empty":
            print(deque.is_empty())
        elif cmd[0] == "pop_front":
            print(deque.Pop_front())
        elif cmd[0] == "pop_back":
            print(deque.Pop_back())
        else:
            print(deque.size)

if __name__== "__main__":
    solve()