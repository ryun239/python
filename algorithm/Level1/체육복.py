
#######################################
############  Note ####################
# 프로그래머스 Lv.1: 신규 아이디 추천
#######################################

def solution(n , lost, reserve):
    answer = 0

    lost_n = list(set(lost) - set(reserve))
    reserve_n = list(set(reserve) - set(lost))

    print(lost_n)
    print(reserve_n)

    cnt = len(lost_n)

    for lost_idx in range(len(lost_n)):
        print("lost_idx" , lost_idx)
        if lost_idx+1 in reserve_n: 
            reserve_n.remove(lost_idx+1)
            print("remove", lost_idx)
            lost_n.remove(lost_idx)

        elif lost_idx-1 in reserve_n: 
            reserve_n.remove(lost_idx-1)
            print("remove", lost_idx)
            lost_n.remove(lost_idx)

    print(lost_n)
    
    #print(n-len(lost_n))
            

if __name__ == "__main__":
    a = 5
    b = [2,4]
    c = [1, 3, 5]
    solution(a,b,c)
