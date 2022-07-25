

from itertools import count


def sol(numbers, target):
    main_node = [0]

    for num in numbers:
        sub_node = []
        for sub in main_node:
            sub_node.append(sub + num)
            sub_node.append(sub - num)
    
        main_node = sub_node


    
    return main_node.count(target)

if __name__ == "__main__":
    a = [4, 1, 2, 1]
    b = 4
    a = [1, 1, 1, 1, 1]	
    b = 3
    ret = sol(a, b)
    print(ret)



