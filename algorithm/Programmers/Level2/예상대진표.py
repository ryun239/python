import random


def com_div(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]

def sol(n, a, b):
    cnt = 1
    com = [a, b]
    com_list = list(range(1, n+1))
    com_list = com_div(com_list, 2)

    while True:
        tmp_list = []
        if com in com_list or com.reverse() in com_list:
            break

        for i in range(len(com_list)):

            if a in com_list[i]:
                tmp_list.append(a)
            elif b in com_list[i]:
                tmp_list.append(b)
            else:
                tmp_list.append(random.choice(com_list[i]))

        tmp_list = com_div(tmp_list, 2)
        com_list = tmp_list
        print(com_list)
        cnt += 1

    return cnt



if __name__ == "__main__":
    a = 10
    b = 1
    c = 3

    ret = sol(a, b, c)
    print(ret)