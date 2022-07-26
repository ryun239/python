

def sol(s):
    ans = []
    zero_cnt = 0
    do_cnt = 0

    while True:
        if s == "1":
            ans.append(do_cnt)
            ans.append(zero_cnt)
            break

        tmp_list = [a for a in s]
        zero_cnt += tmp_list.count("0")
        print(zero_cnt)

        print(s)
        s = s.replace("0", "")
        print(s)

        s = str(bin(len(s)))[2:]
        do_cnt += 1
    return ans





if __name__ == "__main__":
    s_bin =  "110010101001"

    ret = sol(s_bin)

    print(ret)