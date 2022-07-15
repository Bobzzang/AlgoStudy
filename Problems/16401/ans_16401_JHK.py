# https://www.acmicpc.net/problem/16401


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])

    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
            continue
        if right[j] > left[i]:
            res.append(left[i])
            i += 1
            continue
        res.append(left[i])
        res.append(right[j])
        i += 1
        j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def check_distr(ManNum, TarCookie, Cookies):
    left = 0
    right = len(Cookies)
    while left < right:
        mid = (left + right) // 2
        if Cookies[mid] >= TarCookie:
            right = mid
        else:
            left = mid + 1

    Idx = right
    ManCnt = 0
    while Idx < len(Cookies):
        # ManCnt += Cookies[Idx] // TarCookie
        # 위 구문으로 아래 53~56번줄을 대체 가능하지만, 더 느림.
        TempCookie = Cookies[Idx]
        while TempCookie >= TarCookie:
            ManCnt += 1
            TempCookie -= TarCookie
            if ManCnt >= ManNum:
                return False
        Idx += 1

    # True when TarCookie is too long
    return ManCnt < ManNum


def find_max_cookie(ManNum, Cookies):
    # left = Cookies[0]
    # 답이 될 수 있는 최솟값은 가장 작은 과자보다 더 작을 수 있다.
    left = 1
    right = Cookies[-1] + 1

    while left < right:
        mid = (left + right) // 2
        if check_distr(ManNum, mid, Cookies):
            right = mid
        else:
            left = mid + 1

    return left - 1


def solve():
    M, N = map(int, input().split())
    Cookies = merge_sort(list(map(int, input().split())))
    print(find_max_cookie(M, Cookies))
    return


if __name__ == "__main__":
    solve()
