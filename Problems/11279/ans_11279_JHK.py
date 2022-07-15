# https://www.acmicpc.net/problem/11279

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.top = None
        self.left = None
        self.right = None


class Heap:
    def __init__(self):
        self.size = 0

    def append(self, data):
        self.size += 1
        if self.size == 1:
            self.root = Node(data)
        else:
            target = self.root
            # root Node를 index 1로 하는 완전 이진 트리
            # append 시 self.size가 index와 같음
            # 이진법으로 전환하여 각 자릿수는 탐색 방향이 됨
            # 0은 왼쪽, 1은 오른쪽
            # ex. index 6 : 0b110 - root 로부터 오른쪽, 오른쪽, 왼쪽에 위치
            dir = bin(self.size)[3:]
            for i, d in enumerate(dir):
                upperNode = target
                # 결과적으로, 추가할 leaf Node의 상위 Node를 찾기 위함 (연결 설정)
                if target.data < data:
                    target.data, data = data, target.data
                    # Max Heap이므로, 넣으려는 data가 기존 데이터보다 큰 경우
                    # 기존 데이터를 대체하고 기존 데이터를 하위 Node로 전달
                if d == "0":
                    target = target.left
                else:
                    target = target.right
            target = Node(data)
            target.top = upperNode
            if d == "0":
                upperNode.left = target
            else:
                upperNode.right = target

    def popMax(self):
        if self.size == 0:
            return 0
        elif self.size == 1:
            self.size -= 1
            result = self.root.data
            self.root = None
        else:
            result = self.root.data
            # 완전 이진 트리를 유지하기 위해 마지막 Node를 삭제
            # Append 시와 비슷하게, 현재의 self.size를 이용하여 마지막 Node를 탐색
            dir = bin(self.size)[3:]
            target = self.root
            for d in dir:
                if d == "0":
                    target = target.left
                else:
                    target = target.right
            if target.top.right == None:
                target.top.left = None
                # 완전 이진 트리이므로, 마지막 Node의 상위 Node의 오른쪽이 비어있으면
                # 마지막 Node는 left
            else:
                target.top.right = None
            target.top = None
            self.root.data = target.data
            # 기존 root data (max값)은 return 으로 넘기며 삭제 될 것이므로,
            # root data를 마지막 Node였던 data 로 대체
            self.heapify_max(self.root)
            # 마지막 Node가 root에 들어가며 Max Heap이 깨졌으므로,
            # root 부터 값을 재할당
            self.size -= 1
        return result

    def command(self, cmd):
        if cmd == 0:
            print(self.popMax())
        else:
            self.append(cmd)

    def heapify_max(self, target):
        if target.left != None and target.right != None:
            if target.left.data > target.right.data:
                swapTarget = target.left
            else:
                swapTarget = target.right
        elif target.left != None:
            swapTarget = target.left
        else:
            swapTarget = None

        if swapTarget != None:
            if target.data < swapTarget.data:
                target.data, swapTarget.data = swapTarget.data, target.data
                self.heapify_max(swapTarget)


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = []
    H = Heap()
    for _ in range(N):
        TC.append(int(input()))
    for cmd in TC:
        H.command(cmd)
    return


if __name__ == "__main__":
    solve()
