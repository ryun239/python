

from itertools import permutations
import math

def primenumber(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
    # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

def sol(n):
    a = []
    n = [ x for x in n]

    for i in range(1, len(n)+1):
        a += list(permutations(n, i))

    new_list =[int(("".join(x))) for x in a]
    print(new_list)
    new_list = list(set(new_list))

    print(new_list)

    cnt = 0
    for i in new_list:
        if i > 2:
            if primenumber(i) == True:
                cnt += 1

    return cnt

if __name__ == "__main__":
    a = "011"
    ret = sol(a)
    print(ret)