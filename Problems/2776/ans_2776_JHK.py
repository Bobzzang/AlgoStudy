# https://www.acmicpc.net/problem/2776


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
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


def bs(Target, RefList):
    left = 0
    right = len(RefList)
    while left < right:
        mid = (left + right) // 2
        if RefList[mid] == Target:
            return 1
        if RefList[mid] > Target:
            right = mid
        else:
            left = mid + 1
    return 0


def check_nums(RefList, ChkList):
    SortedRef = merge_sort(RefList)
    for c in ChkList:
        print(bs(c, SortedRef))
    return


def solve():
    TC_NUM = int(input())
    RefList = []
    CheckList = []
    for _ in range(TC_NUM):
        N = int(input())
        RefList.append(list(map(int, input().split())))
        M = int(input())
        CheckList.append(list(map(int, input().split())))

    for i in range(TC_NUM):
        check_nums(RefList[i], CheckList[i])
    return


if __name__ == "__main__":
    solve()
