from collections import deque

def sol(N, M, maps):
    map_list = []
    for i in maps:
        tmp = []
        for j in i:
            tmp.append(int(j))
        map_list.append(tmp)

    row = len(maps)
    col = len(maps[0])
    
    graph = [[ -1 for _ in range(col)] for j in range(row)]
    graph[0][0] = 1

    dx = [-1, 1 , 0, 0]
    dy = [0, 0 , -1, 1]

    queue = deque()
    queue.append([0, 0])

    while queue:
        y, x = queue.popleft()
        
        for idx in range(len(dx)):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if 0 <= ny < row and 0 <= nx < col and map_list[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    return graph[N-1][M-1]

if __name__ == "__main__":
    # ex) 1
    a = 4 
    b = 6
    c = ["101111","101010","101011","111011"]
    ret = sol(a, b, c)
    print(ret)

    # ex) 2
    a = 4 
    b = 6
    c = ["110110","110110","111111","111101"]
    ret = sol(a, b, c)
    print(ret)

    # ex) 3
    a = 2 
    b = 25
    c = ["1011101110111011101110111","1110111011101110111011101"]
    ret = sol(a, b, c)
    print(ret)

    # ex) 4
    a = 7 
    b = 7
    c = ["1011111","1110001","1000001","1000001","1000001","1000001","1111111"]
    ret = sol(a, b, c)
    print(ret)
