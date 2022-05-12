
#######################################
############  Note ####################
# 프로그래머스 Lv.1: 신규 아이디 추천
#######################################

def solution(board, moves):
    answer = 0
    stack_list = []
    idx = 0
    
    for move in moves:
        for idx in range(len(board)):
            if board[idx][move -1] == 0:
                pass
            else:
                stack_list.append(board[idx][move-1])
                board[idx][move-1] = 0
                break

        if len(stack_list) >= 2 and stack_list[len(stack_list)-1] == stack_list[len(stack_list) -2]:
            stack_list.pop()
            stack_list.pop()
            answer += 2


    return answer
    

if __name__ == "__main__":
    a = [
         [0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]
         ]

    b = [1,5,3,5,1,2,1,4]

    ret = -1
    ret = solution(a, b)
    print(ret)
