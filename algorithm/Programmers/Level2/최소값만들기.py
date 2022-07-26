
def sol(A,B):
    ans = 0
    a = sorted(A)
    b = sorted(B, reverse=True)

    print(a, b)


    return sum([a * b for a, b in zip(a, b)])


if __name__ == "__main__":
    n = [1, 4, 2]
    k = [5, 4, 4]


    ret=sol(n, k)
    print(ret)