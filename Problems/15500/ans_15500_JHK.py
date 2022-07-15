# https://www.acmicpc.net/problem/15500


def solve():
    N = int(input())
    APoll = list(map(int, input().split()))
    BPoll = []
    CPoll = []
    K = 0
    TargetPlate = N
    Log = []
    while APoll or BPoll:
        if TargetPlate in APoll:
            while APoll[-1] != TargetPlate:
                BPoll.append(APoll.pop())
                Log.append("1 2")
                K += 1
            CPoll.append(APoll.pop())
            Log.append("1 3")
            K += 1
            TargetPlate -= 1
        else:
            while BPoll[-1] != TargetPlate:
                APoll.append(BPoll.pop())
                Log.append("2 1")
                K += 1
            CPoll.append(BPoll.pop())
            Log.append("2 3")
            K += 1
            TargetPlate -= 1
    print(K)
    for l in Log:
        print(l)
    return


if __name__ == "__main__":
    solve()
