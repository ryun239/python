

def sol(s):
    answer = ""
    tmp = s.split(" ")

    tmp = [int(i) for i in tmp]

    
    t_min = min(tmp)
    t_max = max(tmp)

    
    my_s =  "".join(str(min(tmp))) + " " + "".join(str(max(tmp)))

    return my_s


if __name__ == "__main__":
    q = "-1 -2 -3 -4"

    ans = sol(q)
    print(ans)