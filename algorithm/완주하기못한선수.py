
#######################################
############  Note ####################
# 프로그래머스 Lv.1: 신규 아이디 추천
#######################################

def solution(a, b):

    ans = ""
    print(a, b)
    a.sort()
    b.sort()
    print(a, b)



    for idx in range(len(b)):
        if a[idx] != b[idx]:
            return (print(a[idx]))

    return print(a[-1])




if __name__ == "__main__":
    a = ["mislav", "stanko", "mislav", "ana"]
    b = ["stanko", "ana", "mislav"]

    solution(a, b)
