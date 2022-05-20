

def sol(n):
    answer = ""
    n.sort()
    n = list(map(str, n))
    print(n)
    n_list = []

    while len(n) == len(n_list):
        for i in range(len(n)-1):
            print(n[i])
            n_list.append(n[i])


    print(n)
    print(n_list)

    return answer

if __name__ == "__main__":
    n = [3, 30, 34, 5, 9]
    ret = sol(n)
    print(ret)