# https://www.acmicpc.net/problem/15973


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return

    def __eq__(self, ref):
        # Overriding of __eq__
        if self.x == ref.x and self.y == ref.y:
            return True
        return False


class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.dl = Point(x1, y1)
        self.dr = Point(x2, y1)
        self.ul = Point(x1, y2)
        self.ur = Point(x2, y2)
        return


class Interact:
    def __init__(self, x1, y1, x2, y2):
        self.p = Rect(x1, y1, x2, y2)

    def check_type(self, x1, y1, x2, y2):
        self.q = Rect(x1, y1, x2, y2)

        if self.is_null():
            print("NULL")
            return
        if self.is_point():
            print("POINT")
            return
        if self.is_line():
            print("LINE")
            return
        # if self.is_face():
        print("FACE")
        return

    def is_null(self):
        if self.q.ur.x < self.p.dl.x:
            return True
        if self.q.ur.y < self.p.dl.y:
            return True
        if self.q.dl.x > self.p.ur.x:
            return True
        if self.q.dl.y > self.p.ur.y:
            return True
        return False

    def is_onLine(self, ref_rec: Rect, tar_rec: Rect):
        if tar_rec.ul.y == ref_rec.dl.y:
            # tar_rec이 ref_rec 아래에 접할 때
            if tar_rec.ul.x >= ref_rec.dl.x and tar_rec.ul.x <= ref_rec.dr.x:
                return True
            if tar_rec.ur.x >= ref_rec.dl.x and tar_rec.ur.x <= ref_rec.dr.x:
                return True
        if tar_rec.dl.y == ref_rec.ul.y:
            # tar_rec이 ref_rec 위에 접할 때
            if tar_rec.dl.x >= ref_rec.ul.x and tar_rec.dl.x <= ref_rec.ur.x:
                return True
            if tar_rec.dr.x >= ref_rec.ul.x and tar_rec.dr.x <= ref_rec.ur.x:
                return True
        if tar_rec.dl.x == ref_rec.dr.x:
            # tar_rec이 ref_rec 오른쪽에 접할 때
            if tar_rec.dl.y >= ref_rec.dr.y and tar_rec.dl.y <= ref_rec.ur.y:
                return True
            if tar_rec.ul.y >= ref_rec.dr.y and tar_rec.ul.y <= ref_rec.ur.y:
                return True
        if tar_rec.dr.x == ref_rec.dl.x:
            # tar_rec이 ref_rec 왼쪽에 접할 때
            if tar_rec.dr.y >= ref_rec.dl.y and tar_rec.dr.y <= ref_rec.ul.y:
                return True
            if tar_rec.ur.y >= ref_rec.dl.y and tar_rec.ur.y <= ref_rec.ul.y:
                return True
        return False

    def is_line(self):
        if self.is_onLine(self.p, self.q) or self.is_onLine(self.q, self.p):
            return True
        return False

    def is_point(self):
        # Point class에서 __eq__를 overriding
        if self.q.dl == self.p.ur:
            return True
        if self.q.dr == self.p.ul:
            return True
        if self.q.ul == self.p.dr:
            return True
        if self.q.ur == self.p.dl:
            return True
        return False


def solve():
    inter = Interact(*list(map(int, input().split())))
    inter.check_type(*list(map(int, input().split())))

    return


def solve2():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a[0] > b[2] or a[2] < b[0] or a[1] > b[3] or a[3] < b[1]:
        print("NULL")
    elif (
        (a[0] == b[2] and a[1] == b[3])
        or (a[2] == b[0] and a[1] == b[3])
        or (a[2] == b[0] and a[3] == b[1])
        or (a[0] == b[2] and a[3] == b[1])
    ):
        print("POINT")
    elif (a[0] == b[2]) or (a[2] == b[0]) or (a[1] == b[3]) or (a[3] == b[1]):
        # 벗어나는 케이스는 NULL 인 경우에서 걸러짐.
        print("LINE")
    else:
        print("FACE")


if __name__ == "__main__":
    # solve()
    solve2()
