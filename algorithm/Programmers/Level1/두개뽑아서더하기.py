
#######################################
############  Note ####################
# 프로그래머스 Lv.1: 신규 아이디 추천
#######################################

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))


if __name__ == "__main__":
    a = [2,1,3,4,1]
    nRet = solution(a)
    print(nRet)
