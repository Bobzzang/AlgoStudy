# https://www.acmicpc.net/problem/2629


def makeAvail2(ref):
    # memoization을 List 이용하여 구현
    memo = [0]
    for r in ref:
        tempList = []
        for i in memo:
            temp = abs(i - r)
            if temp not in memo:
                # 중복 제거
                tempList.append(temp)
            temp = i + r
            if temp not in memo:
                tempList.append(temp)
        memo = memo + tempList
    return memo


def makeAvail(ref):
    # memoization을 Set 이용하여 구현
    memo = {0}
    for r in ref:
        tempSet = set()
        for i in memo:
            tempSet.update([abs(i - r), i + r])
            # 기존 가능한 것들 중에서 현재 값을 빼거나(반대쪽에 올림) 더하는 경우가 가능
        memo = memo | tempSet
        # 기존 가능한 값과 합치기
    return memo


def solve():
    N = int(input())
    ref = list(map(int, input().split()))
    M = int(input())
    target = list(map(int, input().split()))
    dic = makeAvail(ref)

    for t in target:
        if t in dic:
            print("Y", end=" ")
        else:
            print("N", end=" ")
    print()
    return


if __name__ == "__main__":
    solve()
