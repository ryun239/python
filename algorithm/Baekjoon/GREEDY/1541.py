import re

def sol(string):
    answer = 0
    my_list = string.split("-")

    # print(my_list)
    tmp =  my_list[0].split("+")

    for i in tmp:
        answer += int(i)

    for i in my_list[1:]:
        tmp =  i.split("+")
        a = 0
        for j in tmp:
            a += int(j)
        answer -= a

    return answer


if __name__ == "__main__":
    a = "55-50+40"
    ret = sol(a)
    print(ret)

    a = "10+20+30+40"
    ret = sol(a)
    print(ret)

    a = "00009-00009"
    ret = sol(a)
    print(ret)