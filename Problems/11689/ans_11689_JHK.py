# https://www.acmicpc.net/problem/11689


def solve():
    N = int(input())
    PrimeNums = []
    res = N
    for i in range(2, 1000000):
        # 중요 Point - 10^6 까지만 소수를 구하면 됨.
        # 소인수분해를 하고 남은 수 (res)가 10^6 보다 큰 경우(반복문 종료되는 경우)
        # 이 나머지는 10^6 이하의 소수로 나누어지지 않으며
        # res^2 가 N의 범위 10^12 보다 크므로 (두번 이상 인수로 사용될 수 없으므로)
        # 남은 res 는 N의 소인수 중 하나이다 (소수이다).
        if res == 1:
            break
        if res % i == 0:
            PrimeNums.append(i)
        while res % i == 0:
            res //= i
    if res != 1:
        PrimeNums.append(res)

    cnt = N
    for p in PrimeNums:
        cnt = cnt - cnt // p
        # 이거 설명하기가 뭔가 어려움.
        # 감각적으로 만든 수식인데 되버린 느낌이라 증명을 못하겠다...
        # 소인수 중 하나로 나누어 떨어지는 숫자의 갯수만큼을 제거
        # 남은 수 중에서 또다른 소인수로 나누어 떨어지는 숫자만큼을 제거
        # 위를 반복하면, 소인수의 조합으로 이루어진(중복 소수)의 갯수는 포함되지 않고
        # 남은 수의 갯수를 찾을 수 있는데... 해놓고도 이게 왜 되는지 모르겠음.

    print(cnt)
    return


if __name__ == "__main__":
    solve()
