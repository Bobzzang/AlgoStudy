# https://www.acmicpc.net/problem/10815


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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

    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))


def bs(arr, v):
    left = 0
    right = len(arr)
    while right - left > 0:
        mid = (left + right) // 2
        if arr[mid] == v:
            return True
        if arr[mid] < v:
            left = mid + 1
        else:
            right = mid
    # mid = (left + right) // 2
    # if arr[mid] == v:
    # return True
    return False


def solve():
    N = int(input())
    HavingCards = list(map(int, input().split()))
    M = int(input())
    CheckingCards = list(map(int, input().split()))
    HavingCards = merge_sort(HavingCards)

    # for i in range(len(CheckingCards) - 1):
    #     print(int(bs(HavingCards, CheckingCards[i])), end=" ")
    # print(int(bs(HavingCards, CheckingCards[i + 1])))
    for c in CheckingCards:
        print(int(bs(HavingCards, c)), end=" ")
    print()
    return


if __name__ == "__main__":
    solve()
