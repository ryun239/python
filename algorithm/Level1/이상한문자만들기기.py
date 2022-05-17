

if __name__ == "__main__":
    answer = []
    s = "try hello world"
    s_list = s.split(' ')
    print(s_list)

    for i in range(len(s_list)):
        ret = ""
        for j in range(len(s_list[i])):
            if j % 2 == 0:
                ret += s_list[i][j].upper()
            else:
                ret += s_list[i][j].lower()
        
        answer.append(ret)
    print(answer)

    aa = ''
    aa = ' '.join(answer)
    print(aa)
