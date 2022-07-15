# https://www.acmicpc.net/problem/3568


def solve():
    sentence = input()
    sentence = sentence.replace(";", "")
    sentence = sentence.replace(",", "")
    words = sentence.split()
    defaultType = words[0]
    vars = words[1:]
    ans = []
    for v in vars:
        stack = []
        i = 0
        varName = ""
        while i < len(v):
            if v[i] == "*" or v[i] == "&":
                stack.append(v[i])
            elif v[i] == "[":
                stack.append("[]")
                i += 1
            else:
                varName += v[i]
            i += 1
        fixedType = defaultType
        while len(stack) > 0:
            fixedType += stack.pop()
        print(fixedType, end=" ")
        print(varName, end="")
        print(";")
    return


if __name__ == "__main__":
    solve()
