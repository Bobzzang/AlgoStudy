# https://www.acmicpc.net/problem/10610


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
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def solve():
    NStr = input()
    Numbers = []
    for n in NStr:
        Numbers.append(int(n))
    Numbers = merge_sort(Numbers)
    if Numbers[-1] != 0:
        print(-1)
        return
    if sum(Numbers) % 3 != 0:
        print(-1)
        return
    for n in Numbers:
        print(n, end="")
    print()
    return


if __name__ == "__main__":
    solve()
