

def sol(A, moneys):
    answer = 0

    for idx in range(len(moneys) -1, -1, -1):
        a, b = divmod(A, moneys[idx])

        if a > 0:
            answer += a
            A = b
            continue

        if a == 0 and b == 0:
            break

    return answer


if __name__ == "__main__":
    a = 50002
    b = [1,5,10,50,100,500,1000,5000,10000,50000]

    ret = sol(a, b)
    print(ret)