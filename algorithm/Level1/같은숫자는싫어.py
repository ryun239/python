

from random import randrange


def sol(arr):
    answer = []

    answer.append(arr[0])

    for idx in range(1, len(arr)):
        if arr[idx] != arr[idx-1]:
            answer.append(arr[idx])
    return answer

if __name__ == "__main__":
    #arr = [1,1,3,3,0,1,1]
    arr = [4,4,4,3,3]
    print(sol(arr))