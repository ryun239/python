
def sol(a, b):

    b_idx = b
    cnt = 1

    while True:
        if a:
            max_val = max(a)
        else:
            break

        if a.index(max_val) == b_idx:
            break
        
        if a.index(a[0]) < a.index(max(a)):
            a.append(a[0])
            a.pop(0)
            if b_idx == 0:
                b_idx = len(a) -1
            else:
                b_idx -= 1
        elif a.index(a[0]) == a.index(max(a)):
            a = a[1:]
            cnt += 1
            if b_idx == 0:
                b_idx = len(a) -1
            else:
                b_idx -= 1

    return cnt

if __name__ == "__main__":
    my_list = [1, 2, 5, 2, 1]
    my_list = [1, 1, 9, 1, 1, 1]
    my_list = [2, 1, 3, 2]
    k = 0
    k = 2

    ret = sol(my_list, k)
    print(ret)
