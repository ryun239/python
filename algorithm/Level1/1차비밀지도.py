

def sol(a, b ,c):
    arr1 = []
    arr2 = []
    ret = []

    for idx in range(a):
        arr1.append((bin(b[idx]))[2:].zfill(a))
        arr2.append((bin(c[idx]))[2:].zfill(a))


    for i in range(a):
        tmp = ""
        for idx in range(a):
            if arr1[i][idx] == "1" or arr2[i][idx] == "1":
                tmp += "".join("#")
            else:
                tmp += "".join(" ")
        ret.append(tmp)
    print(ret)

if __name__ == "__main__":
    a = 5
    b = [9, 20, 28, 18, 11]
    c = [30, 1, 21, 17, 28]
    ret = sol(a, b, c)
    print(ret)
