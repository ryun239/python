

def sol(n):
    answer_list = []

    while n > 0:
        n, mod = divmod(n, 124)
        print(n, mod)
        answer_list.append(mod)
    print(answer_list)


if __name__ == "__main__":
    n = 10
    ret = sol(n)
    print(ret)