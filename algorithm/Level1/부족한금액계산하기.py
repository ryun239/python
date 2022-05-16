

def sol(price, money, count):
    answer = 0
    total = 0

    for cnt in range(1, count+1):
        total += price * cnt
    
    if total <= money:
        return 0
    else:
        answer = total - money
        return answer

if __name__ == "__main__":
    a = 3
    b = 20
    c = 4
    print(sol(a, b, c))