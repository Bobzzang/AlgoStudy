# https://www.acmicpc.net/problem/2343


def checkDiskStorage(Lectures, disk, storgLimit):
    res = 1
    Storage = 0
    for lect in Lectures:
        if lect > storgLimit:
            return False
        if Storage + lect <= storgLimit:
            Storage += lect
        else:
            Storage = lect
            res += 1

    if res <= disk:
        return True
    else:
        return False


def bs(Lectures, disk):
    left = 0
    right = sum(Lectures) + 1
    while left < right:
        mid = (left + right) // 2
        if checkDiskStorage(Lectures, disk, mid):
            right = mid
        else:
            left = mid + 1
    return right


def solve():
    N, M = map(int, input().split())
    Lectures = list(map(int, input().split()))
    print(bs(Lectures, M))
    return


if __name__ == "__main__":
    solve()
