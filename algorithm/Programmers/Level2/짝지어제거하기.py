

def sol(s):
    my_stack = []

    for word in s:
        if len(my_stack) == 0:
            my_stack.append(word)
        elif my_stack[-1] == word:
            my_stack.pop(-1)
        else:
            my_stack.append(word)
    if my_stack:
        return 0
    else:
        return 1



if __name__ == "__main__":
    a = "baabaa"
    ret = sol(a)
    print(ret)