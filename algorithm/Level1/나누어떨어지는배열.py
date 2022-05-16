

from ast import AnnAssign


def sol(arr, divisor):
    answer = []

    for val in arr:
        if not val % divisor:
            answer.append(val)
    
    if not answer:
        answer = -1
    else:
        answer.sort()
    
    print(answer)
    return answer


if __name__ == "__main__":
    arr = [5, 9, 7, 10]
    #arr = [2, 36, 1, 3]


    divisor = 5
    sol(arr, divisor)