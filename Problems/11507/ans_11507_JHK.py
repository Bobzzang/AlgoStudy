# https://www.acmicpc.net/problem/11507


def solve():
    s = input().rstrip()
    Cards = []
    for i in range(0, len(s), 3):
        Cards.append(s[i : i + 3])

    LostP = 0
    LostK = 0
    LostH = 0
    LostT = 0
    for Card in Cards:
        mask = 1 << (int(Card[1:]) - 1)
        if Card[0] == "P":
            if LostP & mask == mask:
                print("GRESKA")
                return
            LostP |= mask
            continue
        if Card[0] == "K":
            if LostK & mask == mask:
                print("GRESKA")
                return
            LostK |= mask
            continue
        if Card[0] == "H":
            if LostH & mask == mask:
                print("GRESKA")
                return
            LostH |= mask
            continue
        if Card[0] == "T":
            if LostT & mask == mask:
                print("GRESKA")
                return
            LostT |= mask
            continue
    print((13 - bin(LostP).count("1")))
    print((13 - bin(LostK).count("1")))
    print((13 - bin(LostH).count("1")))
    print((13 - bin(LostT).count("1")))
    return


if __name__ == "__main__":
    solve()
