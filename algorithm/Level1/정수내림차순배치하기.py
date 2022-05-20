

def sol(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)

    return int("".join(n_list))

    

if __name__ == "__main__":
    n = 118372
    ret = -1
    ret = sol(n)

    print(ret)
    n = 12

    n_list = list(map(int ,str(n)))
    print(n_list)
