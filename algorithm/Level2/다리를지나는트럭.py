
def sol(length, w, trucks):
    cnt = 0
    bridge = [0 for _ in range(length)]

    while bridge:
        cnt += 1
        bridge.pop(0)

        if trucks:
            if sum(bridge) + trucks[0] <= w:
                bridge.append(trucks.pop(0))
            else:
                bridge.append(0)
    
    return cnt
    





if __name__ == "__main__":
    # a = 2
    # b = 10
    # c = [7,4,5,6]
    a = 100
    b = 100
    # c = [10,10,10,10,10,10,10,10,10,10]	
    c = [10]

    ret = sol(a, b, c)
    print(ret)