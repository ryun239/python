from math import gcd, lcm

def sol(a):
    answer = a[0]
    
    for i in a:
        print(i * answer)
        print(gcd(i, answer))

        answer = (i * answer) // (gcd(i, answer))
        print("--------")
    
    return answer 


if __name__ == "__main__":
    a = [2,6,8,14]
    
    ret = sol(a)
    print("Final = :",ret)