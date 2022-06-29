

def sol(k, arr):
    answer = 0
    ph = []
    ex = []
    for i in range(len(arr)):
        ph.append(arr[i][0])
        ex.append(arr[i][1])
    
    for i in range(len(arr)):
        if k >= max(ph):
            idx = ph.index(max(ph))
            k = k - ex[idx]
            ph.remove(max(ph))
            answer += 1


    return answer

if __name__ == "__main__":
    arr = [[80,20],[50,40],[30,10]] 
    k = 80

    ret = sol(k, arr)
    print(ret)

