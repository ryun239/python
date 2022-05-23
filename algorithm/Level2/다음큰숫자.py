
def sol(n):
    answer = 0
    new_n = bin(n).count("1")

    while True:
        n = n+1

        if new_n == bin(n).count("1"):
            answer = n

        if answer:
            break


    return answer

if __name__ == "__main__":
    n = 15
    #n = 78
    ret = sol(n)
    print(ret)