

def solution(d, budget):
    answer = 0
    cnt = 0

    for part in d:
        if part >= budget:
            break
        else:
            budget -= part
            cnt += 1

    answer = cnt
    print(answer)


    return answer

if __name__ == "__main__":
    a = [2, 2, 3, 3] 
    b = 10

    solution(a, b)
