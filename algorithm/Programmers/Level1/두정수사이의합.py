


def sol(a, b):
    answer = 0

    if a > b:
        a,b = b,a

    return sum(range(a, b+1))


if __name__ == "__main__":
    a = 3
    b =5
    print(sol(a,b))