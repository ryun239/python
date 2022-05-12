
#######################################
############  Note ####################
# 프로그래머스 Lv.1: 신규 아이디 추천
#######################################

def solution(array, commands):
    answer = []
    

#    print(array)
#    for i in commands:
#        a = i[0] -1
#        b = i[1]
#        c = i[2] - 1
#
#        tmp_list = array[a:b]
#        tmp_list.sort()
#
#        answer.append( tmp_list[c] )

    answer =  list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


    print(answer)
        


if __name__ == "__main__":

    a =  [1, 5, 2, 6, 3, 7, 4]
    b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    solution(a, b)
