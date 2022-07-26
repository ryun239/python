

from re import I


def sol(s, trees):
    answer = 0

    for tree in trees:
        cmp = list(s)
        for t in tree:
            if t in cmp:
                if t != cmp.pop(0):
                    break
        else:
            answer += 1

    return answer



if __name__ == "__main__":
    a = "CBD"
    b = ["BACDE", "CBADF", "AECB", "BDA", "CBD", "C"]

    a = "ZDB"
    b = ["ZEQG", "DEGQ", "PIEZB", "MNZQEDOIB"]

    ret = sol(a, b)
    print(ret)