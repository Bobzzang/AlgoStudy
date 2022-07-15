# https://www.acmicpc.net/problem/23322

# 괜히 복잡해보이는 문제
# 결과적으로 모든 초콜릿 수는 첫번째 초콜릿 수와 동일하게 되며,
# 일수를 최소화 하기 위해서는 한번 선택 한 통을 최대한 먹어야 함.
# 먼저, K번째 통을 반복해서 선택하면 K 이하의 통이 첫번째 통의 갯수로 맞춰지고(1일1통)
# 이후 나머지 통을 K+1 부터 순서대로 선택하면 됨.
# 이와 같이 선택 할 경우,
# 일수는 첫번째 통보다 많은 통의 갯수와 같다.


def solve():
    N, K = map(int, input().split())
    Choco = list(map(int, input().split()))
    Days = 0
    NumEat = 0
    for i in range(1, len(Choco)):
        if Choco[i] > Choco[0]:
            Days += 1
            NumEat += Choco[i] - Choco[0]
    print(f"{NumEat} {Days}")
    return


if __name__ == "__main__":
    solve()
