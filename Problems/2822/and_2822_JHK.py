# https://www.acmicpc.net/problem/2822


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


def solve():
    Score = [int(input()) for _ in range(8)]
    SortedScore = merge_sort(Score)
    print(sum(SortedScore[3:]))
    for i, s in enumerate(Score):
        if s in SortedScore[3:]:
            print(i + 1)
    return


if __name__ == "__main__":
    solve()
