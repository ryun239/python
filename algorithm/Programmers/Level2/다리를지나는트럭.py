
def sol(length, w, trucks):
    bridge = [0 for _ in range(length)]
    answer = 0

    while bridge:
        answer += 1
        bridge.pop(0)

        if trucks:
            if sum(bridge) + trucks[0] <= w:
                bridge.append(trucks.pop(0))
            else:
                bridge.append(0)

    return answer

if __name__ == "__main__":
    a = 2
    b = 10
    c = [7,4,5,6]

    ret = sol(a, b, c)
    print(ret)