
def sol(N):
    answer = 1
    B = 5
    S = 3
    
    cal = [N]

    while True:
        if sum(cal) < 0:
            answer = -1
            break

        tmp = []
        if 5 in cal or 3 in cal:
            break
        else:
            for i in cal:
                tmp.append(i - S)
                tmp.append(i - B)
        cal = tmp

        answer += 1

    return answer



if __name__ == "__main__":
    # a = 18
    # ret = sol(a)
    # print(ret)

    # a = 4
    # ret = sol(a)
    # print(ret)

    a = 6
    ret = sol(a)
    print(ret)

    # a = 9
    # ret = sol(a)
    # print(ret)

    # a = 11
    # ret = sol(a)
    # print(ret)


