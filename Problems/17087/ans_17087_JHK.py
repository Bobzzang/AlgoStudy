# https://www.acmicpc.net/problem/17087


def merge_sort(arr):
    def merge(left, right):
        leftIdx = 0
        rightIdx = 0
        ret = []
        while leftIdx < len(left) and rightIdx < len(right):
            if left[leftIdx] < right[rightIdx]:
                ret.append(left[leftIdx])
                leftIdx += 1
            else:
                ret.append(right[rightIdx])
                rightIdx += 1

        while leftIdx < len(left):
            ret.append(left[leftIdx])
            leftIdx += 1
        while rightIdx < len(right):
            ret.append(right[rightIdx])
            rightIdx += 1
        return ret

    if len(arr) <= 1:
        return arr
    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))


def solve():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    for i, v in enumerate(A):
        A[i] = abs(v - S)
    if len(A) == 1:
        print(A[0])
        return
    A = merge_sort(A)
    p = A[0]
    i = 1
    while i < len(A):
        q = A[i]
        while p != 0:
            q, p = p, q % p
        p = q
        i += 1
    print(p)
    return


if __name__ == "__main__":
    solve()
