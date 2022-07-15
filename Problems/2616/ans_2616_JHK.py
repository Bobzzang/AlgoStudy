# https://www.acmicpc.net/problem/2616


def get_max_passenger(PSum, MaxTrain, RemainTrain, StartTrain, dic):
    # Top down으로 풀어도 계산량은 비슷한 것 같은데... Time out
    if RemainTrain == 0:
        return 0
    if StartTrain >= len(PSum):
        return 0
    if dic[RemainTrain - 1][StartTrain] != None:
        return dic[RemainTrain - 1][StartTrain]
    max_passenger = 0
    for i in range(StartTrain, len(PSum)):
        temp_pass = PSum[i] + get_max_passenger(
            PSum, MaxTrain, RemainTrain - 1, i + MaxTrain, dic
        )

        if max_passenger < temp_pass:
            max_passenger = temp_pass
    dic[RemainTrain - 1][StartTrain] = max_passenger
    return max_passenger


def solve():
    N = int(input())
    Trains = list(map(int, input().split()))
    MaxTrain = int(input())
    PassengerSum = []
    TempSum = 0
    for i in range(MaxTrain):
        TempSum += Trains[i]
    PassengerSum.append(TempSum)
    for i in range(len(Trains) - MaxTrain):
        TempSum += Trains[i + MaxTrain] - Trains[i]
        PassengerSum.append(TempSum)

    # dic = [[None] * (len(PassengerSum)) for _ in range(3)]
    # print(get_max_passenger(PassengerSum, MaxTrain, 3, 0, dic))
    dic = [[0] * (len(PassengerSum)) for _ in range(3)]
    for tr in range(3):
        for i in range(len(PassengerSum)):
            if i < tr * MaxTrain:
                # index error 방지 위한 선처리 (초기값 0 이용)
                continue
            if i == 0:
                dic[tr][i] = PassengerSum[i]
                continue
            if tr == 0:
                # i번째 기차를 첫번째 기차 선택 했을 때 vs 그 이전에 선택했을 때의 최댓값
                dic[tr][i] = max(PassengerSum[i], dic[tr][i - 1])
                continue
            # 2,3번째 기차 선택 시 - i번째 기차 선택 한 경우 vs 선택하지 않은 경우
            dic[tr][i] = max(
                PassengerSum[i] + dic[tr - 1][i - MaxTrain], dic[tr][i - 1]
            )

    print(dic[-1][-1])
    return


if __name__ == "__main__":
    solve()
