# https://www.acmicpc.net/problem/2417


def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    length = len(str(N)) - 1
    left = 10 ** (length // 2)
    right = 10 ** (length // 2 + 1)
    while left < right:
        mid = (left + right) // 2
        CheckVal = mid ** 2
        if CheckVal > N:
            right = mid
        elif CheckVal < N:
            left = mid + 1
        else:
            print(mid)
            return
    print(right)
    return


if __name__ == "__main__":
    solve()
