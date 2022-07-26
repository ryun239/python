

def sol(n):
    ans = 0
    for i in range(1, n+1):
        tmp_list = []
        for j in range(i, n+1):
            tmp_list.append(j)
            if sum(tmp_list) > 15:
                break
            elif sum(tmp_list) == 15:
                ans += 1

                break
            else:
                continue
    return ans


if __name__ == "__main__":
    n = 15
    ret = sol(n)
    print(ret)