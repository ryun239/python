from collections import deque

def sol(N, maps):
    # maps
    #    0  1  2  3  4  5  6
    # 0 [0, 1, 1, 0, 1, 0, 0] 
    # 1 [0, 1, 1, 0, 1, 0, 1] 
    # 2 [1, 1, 1, 0, 1, 0, 1] 
    # 3 [0, 0, 0, 0, 1, 1, 1] 
    # 4 [0, 1, 0, 0, 0, 0, 0] 
    # 5 [0, 1, 1, 1, 1, 1, 0] 
    # 6 [0, 1, 1, 1, 0, 0, 0]
    
    # string_list to int_list
    map_list = []
    for map in maps:
        tmp = []
        for m in map:
            tmp.append(int(m))
        map_list.append(tmp)

    rows = len(maps)
    cols = len(maps[0])

    apt = []
    graph = [[ -1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # 방문한 아파트 좌표 리스트
    visit_list = []

    # 아파트가 있는 곳 찾을 방향
    queue = deque()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for row in range(rows) :
        for col in range(cols): 
            # 아파트 있는곳 찾기
            if map_list[row][col] == 1 and [row, col] not in visit_list:
                queue.append([row, col])
                graph[row][col] = 1
                visit_list.append([row, col])

                # 인접한 아파트 순회하기
                tmp = [[row, col]]
                while queue:
                    y , x = queue.popleft()
                    for idx in range(len(dx)):
                        nx = x + dx[idx]
                        ny = y + dy[idx]

                        if 0 <= nx < cols and 0 <= ny < rows and map_list[ny][nx] == 1:
                            if graph[ny][nx] == -1:
                                visit_list.append([ny, nx])
                                graph[ny][nx] = graph[y][x] + 1
                                queue.append([ny, nx])
                                tmp.append([ny, nx])
                apt.append(len(tmp))
    
    group = str(len(apt))
    cnt = " ".join([str(_) for _ in apt])

    print(group, cnt)

if __name__ == "__main__":
    a = 7
    b = ["0110100","0110101","1110101","0000111","0100000","0111110","0111000"]
    ret = sol(a, b)