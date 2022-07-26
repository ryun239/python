


def IsCorrect(s):
    a_cnt = s.count("[")
    b_cnt = s.count("]")

    if a_cnt != b_cnt:
        return False

    a_cnt = s.count("{")
    b_cnt = s.count("}")

    if a_cnt != b_cnt:
        return False

    a_cnt = s.count("(")
    b_cnt = s.count(")")

    if a_cnt != b_cnt:
        return False

    return True

def IsFine(s):
    stack = []

    for item in s:
        stack.append(item)

        if len(stack) >= 2:
            tmp_str = "".join(stack[-2:])

            if tmp_str == "()" or tmp_str == "[]" or tmp_str == "{}":
                stack.pop()
                stack.pop()
    
    if not stack:
        return True
    else:
        return False



def sol(s):
    if not IsCorrect(s):
        return 0

    cnt = 0
    
    for i in range(len(s)):
        print(s)
        if IsFine(s) == True:
            cnt += 1
        s += "".join(s[0])
        s = s[1:]
    
    return cnt



    

if __name__ == "__main__":
    s = "[](){}"
    # s = "}]()[{"
    # s = "[)(]"
    # s = "}}}"
    ret = sol(s)
    print(ret)