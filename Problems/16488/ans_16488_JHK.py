# https://www.acmicpc.net/problem/16488

# 이등변 삼각형 ABC (AB=AC) 에서
# 밑변(BC)에 대한 한 점 P에 대해
# BC의 중점을 M이라 할 때,
# BP = a, PM = b, MC = c, AM = h 라 하면 (P가 BM 위에 있을 경우)
# 문제에서 제시된 수식 F(i)는
# F(i) = AP^2 + a*(b+c)
# c = a+b 이고, AP^2 = PM^2 + AM^2 이므로
# F(i) = b^2 + h^2 + a*(a+2b)
#      = a^2 + 2ab + b^2 +h^2
#      = (a+b)^2 + h^2
#      = c^2 + h^2
#      = AC^2
#      = N^2


def solve():
    N, K = map(int, input().split())
    print(N ** 2 * K)
    return


if __name__ == "__main__":
    solve()
