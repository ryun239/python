
import math

def sol(n):
    answer = 0 
    n.sort()
    answer = n[0]

    for i in n:
        answer = (i * answer) // math.gcd(i, answer)

    return answer

if __name__ == "__main__":
    n = [2,6,8,14]	
    ret = sol(n)
    print(ret)