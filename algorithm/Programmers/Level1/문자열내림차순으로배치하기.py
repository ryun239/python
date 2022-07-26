



if __name__ == "__main__":
    s = "ZbcAdefg"

    upper_list = []
    lower_list = []

    for word in s:
        if word.isupper():
            upper_list.append(word)
        else:
            lower_list.append(word)

    upper_list.sort(reverse=True)
    lower_list.sort(reverse=False)

    print(lower_list)
    lower_list += upper_list
    print(lower_list)

    answer = ""
    answer = "".join(s for s in lower_list)
    print(answer)


    answer = "".join(sorted(s, reverse=True))
    print(answer)

