
#######################################
############  Note ####################
# 프로그래머스 Lv.1: 신규 아이디 추천
#######################################

def solution(left, right):

    answer = 0
    sum_list = []
    range_list = list(range(1, 1001))
    tmp_list = range_list[left-1: right]
    cnt = 0

    for i in tmp_list:
        for j in range(1, right+1):
            if i % j == 0:
                cnt += 1

        print(i, cnt)
        if cnt % 2 == 0:
            sum_list.append(i)
        else:
            sum_list.append(-i)

        cnt = 0

    answer = sum(sum_list)
    print(type(answer))
    print(sum_list)




if __name__ == "__main__":
    a = 13
    b = 17
    solution(a, b)
