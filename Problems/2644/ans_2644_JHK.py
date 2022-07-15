# https://www.acmicpc.net/problem/2644

import sys


class Person:
    def __init__(self, name):
        self.name = name
        self.Parent = None
        self.Childs = []
        self.visited = False

    def set_parent(self, Parent: "Person"):
        self.Parent = Parent
        self.Parent.__set_child(self)

    def __set_child(self, Child: "Person"):
        self.Childs.append(Child)
        return

    def search(self, target):
        if self.visited:
            return 0
        self.visited = True
        if self.name == target:
            return 1
        if self.Parent != None:
            cnt = self.Parent.search(target)
            if cnt > 0:
                return cnt + 1
        for Child in self.Childs:
            cnt = Child.search(target)
            if cnt > 0:
                return cnt + 1

        return 0


def solve():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A, B = map(int, input().split())
    Num_Relations = int(input().rstrip())
    People = [Person(x) for x in range(N + 1)]
    for _ in range(Num_Relations):
        ParentName, ChildName = map(int, input().split())
        People[ChildName].set_parent(People[ParentName])
    cnt = People[A].search(B)
    if cnt > 0:
        print(cnt - 1)
    else:
        print(-1)
    return


if __name__ == "__main__":
    solve()
