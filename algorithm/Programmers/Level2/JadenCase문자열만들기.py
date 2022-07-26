

def sol(s):
    answer = ""
    print(s)
    s = s.split(" ")
    print(s)

    for i in range(len(s)):
        print(i)
        s[i] = s[i].capitalize()
    print(s)

    return answer


if __name__ == "__main__":
    #s = "3people unFollowed me"
    s = "for the last week" 
    ret = sol(s)