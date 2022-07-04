

def sol(numbers, target):
    main_node = [0]

    for num in numbers:
        sub_node = []
        for sub in main_node:
            sub_node.append(sub + num)
            sub_node.append(sub - num)

        main_node = sub_node
        print(main_node)

if __name__ == "__main__":
    a = [4, 1, 2, 1]
    b = 2
    ret = sol(a, b)
    print(ret)