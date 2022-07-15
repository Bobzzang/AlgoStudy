# https://www.acmicpc.net/problem/1064


def calc_side_grad(p1, q1, p2, q2):
    side = ((p2 - p1) ** 2 + (q2 - q1) ** 2) ** 0.5
    if p2 == p1:
        return side, 10001
    if p2 > p1:
        return side, (q2 - q1) / (p2 - p1)
    return side, (q1 - q2) / (p1 - p2)


def is_triangle(s1, s2, s3):
    # s1 <= s2 <= s3  by sorted input
    return s3 < s1 + s2
    # 왠지 모르겠지만 안됨... 기울기 체크로 바꿈.


def solve():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    Sides = []
    Sides.append(calc_side_grad(x1, y1, x2, y2))
    Sides.append(calc_side_grad(x2, y2, x3, y3))
    Sides.append(calc_side_grad(x3, y3, x1, y1))
    Sides.sort()
    if Sides[0][1] == Sides[1][1] and Sides[1][1] == Sides[2][1]:
        print(-1)
        return
    print(((Sides[2][0] - Sides[0][0]) * 2) * (10 ** 9) // 1 / (10 ** 9))
    return


if __name__ == "__main__":
    solve()
