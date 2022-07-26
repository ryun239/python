

from turtle import pencolor


def sol(peple, limit):
    answer = 0
    peple.sort()

    start = 0
    end   = len(peple) -1

    while start <= end:
        answer += 1
        if peple[start] + peple[end] <= limit:
            start += 1
        end -= 1

    return answer





if __name__ == "__main__":
    a = [70, 50, 80, 50]
    b = 100

    ret = sol(a, b)
    print(ret)
