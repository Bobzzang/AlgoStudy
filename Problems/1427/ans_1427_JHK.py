# https://www.acmicpc.net/problem/1427


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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

    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))


def solve():
    S = input()
    Nums = []
    for c in S:
        Nums.append(int(c))
    Nums = merge_sort(Nums)
    for n in Nums:
        print(n, end="")
    print()
    return


if __name__ == "__main__":
    solve()
