# https://www.acmicpc.net/problem/1940


def merge_sort(arr):
    def merge(left, right):
        leftIdx = 0
        rightIdx = 0
        res = []
        while leftIdx < len(left) and rightIdx < len(right):
            if left[leftIdx] >= right[rightIdx]:
                res.append(right[rightIdx])
                rightIdx += 1
            else:
                res.append(left[leftIdx])
                leftIdx += 1
        while leftIdx < len(left):
            res.append(left[leftIdx])
            leftIdx += 1
        while rightIdx < len(right):
            res.append(right[rightIdx])
            rightIdx += 1
        return res

    if len(arr) <= 1:
        return arr

    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))


def solve():
    N = int(input())
    M = int(input())
    Ing = list(map(int, input().split()))
    Ing = merge_sort(Ing)
    cnt = 0

    left = 0
    right = N - 1
    while left < right:
        val = Ing[left] + Ing[right]
        if val == M:
            cnt += 1
            left += 1
            right -= 1
        elif val < M:
            left += 1
        else:
            right -= 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
