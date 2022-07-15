# https://www.acmicpc.net/problem/1260

from os import link
import sys


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = QueueNode(None)
        self.tail = QueueNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def put(self, data):
        NewNode = QueueNode(data)
        OldNode = self.tail.prev
        NewNode.next = self.tail
        NewNode.prev = OldNode
        OldNode.next = NewNode
        self.tail.prev = NewNode
        self.size += 1

    def get(self):
        if self.size != 0:
            tarNode = self.head.next
            nextNode = tarNode.next
            res = tarNode.data
            self.head.next = nextNode
            nextNode.prev = self.head
            self.size -= 1
            return res


class Node:
    def __init__(self, num):
        self.num = num
        self.edge = []
        self.NotVisited = True

    def linkEdge(self, tar):
        self.edge.append(tar)
        self.edge.sort(key=lambda x: x.num)


class Graph:
    def __init__(self):
        self.NodeList = [None]
        self.queue = Queue()

    def setNewList(self, N):
        for i in range(1, N + 1):
            self.NodeList.append(Node(i))

    def linkEdges(self, link):
        NodeA = self.NodeList[link[0]]
        NodeB = self.NodeList[link[1]]
        NodeA.linkEdge(NodeB)
        NodeB.linkEdge(NodeA)

    def clearAllVisit(self):
        for Node in self.NodeList:
            if Node is not None:
                Node.NotVisited = True

    def DFS(self, startNode):
        tarNode = self.NodeList[startNode]
        if tarNode.NotVisited:
            print(tarNode.num, end=" ")
            tarNode.NotVisited = False
            for linkedNode in tarNode.edge:
                self.DFS(linkedNode.num)

    def BFS(self, startNode):
        tarNode = self.NodeList[startNode]
        tarNode.NotVisited = False
        self.queue.put(tarNode.num)
        while self.queue.size != 0:
            tar = self.queue.get()
            print(tar, end=" ")
            newTarNode = self.NodeList[tar]
            for n in newTarNode.edge:
                if n.NotVisited:
                    n.NotVisited = False
                    self.queue.put(n.num)


def solve():
    input = sys.stdin.readline
    N, M, V = map(int, input().split())
    G = Graph()
    G.setNewList(N)
    for _ in range(M):
        tempLink = list(map(int, input().split()))
        G.linkEdges(tempLink)
    G.DFS(V)
    print()
    G.clearAllVisit()
    G.BFS(V)
    print()
    return


if __name__ == "__main__":
    solve()
