
def solution(n):
    answer = 0
    x = 1

    while not answer:
        if n % x == 1:
            answer = x
            break
        else:
            x +=1

    return answer

if __name__ == "__main__":
    a = 12
    print(solution(a))