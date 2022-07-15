# https://www.acmicpc.net/problem/11004


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
        else:
            res.append(left[i])
            i += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def solve():
    N, K = map(int, input().split())
    Arr = merge_sort(list(map(int, input().split())))
    print(Arr[K - 1])
    return


if __name__ == "__main__":
    solve()
