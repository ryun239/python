

def sol(n):
    answer = ""

    print(n)
    new_num = "*" * (len(n) -4) + n[-4:] 
    print(new_num)

    return answer


if __name__ == "__main__":
    n = "01012341234"

    sol(n)