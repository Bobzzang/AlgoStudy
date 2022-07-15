# https://www.acmicpc.net/problem/2606

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.NotVisited = True
        self.edges = []


class Graph:
    def __init__(self):
        self.Nodes = {}
        self.NumInfected = 0

    # def appendNode(self, NodeNum):
    #     self.Nodes[NodeNum] = Node(NodeNum)

    def linkEdge(self, link):
        Node1Num = link[0]
        Node2Num = link[1]
        # 어차피 1번 Node에 연결된 내용만이 필요하므로, 모든 노드를 생성 할 필요는 없음(Line 48~49, self.appendNode)
        if Node1Num not in self.Nodes:
            self.Nodes[Node1Num] = Node(Node1Num)
        if Node2Num not in self.Nodes:
            self.Nodes[Node2Num] = Node(Node2Num)
        self.Nodes[Node1Num].edges.append(self.Nodes[Node2Num])
        self.Nodes[Node2Num].edges.append(self.Nodes[Node1Num])

    def InfectFrom(self, ComNum):
        # 깊이우선탐색
        targetNode = self.Nodes[ComNum]
        if targetNode.NotVisited:
            targetNode.NotVisited = False
            self.NumInfected += 1
            for node in targetNode.edges:
                self.InfectFrom(node.data)
        return self.NumInfected


def solve():
    input = sys.stdin.readline
    NodeNum = int(input())
    LinkNum = int(input())
    G = Graph()
    # for i in range(1, NodeNum + 1):
    #     G.appendNode(i)
    for _ in range(LinkNum):
        G.linkEdge(list(map(int, input().split())))
    print(G.InfectFrom(1) - 1)
    # 1번 컴퓨터가 "감염시킨" 컴퓨터의 수이므로 1번 컴퓨터 자신은 카운트 제외
    return


if __name__ == "__main__":
    solve()
