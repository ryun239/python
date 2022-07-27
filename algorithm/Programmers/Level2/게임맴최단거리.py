from collections import deque

def solution(maps):
    answer = 0
    
    graph = [[-1 for _ in range(len(maps))] for _ in range(len(maps[0]))]
    graph[0][0] = 1
    
    for g in graph:
        print(g)
    dq = deque()
    dq.append([0, 0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while dq:
        y, x = dq.popleft()
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and maps[y][x] == 1:
                if graph[ny][nx] == -1:
                    dq.append([ny, nx])
                    graph[ny][nx] = graph[y][x] + 1
    
    
    for g in graph:
        print(g)
    answer = graph[-1][-1]
    return answer


if __name__ == "__main__":
    a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
    a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    ret = solution(a)
    print(ret)