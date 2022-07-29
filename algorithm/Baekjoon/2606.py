from collections import deque
import time


def sol(N, links):
    start = time.time()
    print(start)
    queue = deque()
    queue.append(1)

    infection = []

    while queue:
        flud = queue.popleft()
        infection.append(flud)

        for link in links:
            a, b = link
            if a == flud and b not in infection:
                queue.append(b)
    
    print("감염 리스트 =", infection)
    print(len(infection) -1)
    end = time.time()

    print("%f ms" %((end-start) * 1000))



if __name__ == "__main__":
    a = 7
    b = [[1, 2],[2, 3],[1, 5],[5, 2],[5, 6],[4, 7]]

    ret = sol(a, b)
