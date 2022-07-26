from collections import deque

# def sol(maps):
#     print(maps)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     r = len(maps)
#     c = len(maps[0])

#     graph = [[0 for _ in range(c)] for _ in range(r)]

#     queue = deque()
#     queue.append([0, 0])

#     graph[0][0] = 1

#     while queue:
#         y, x = queue.popleft()

#         # 현재 위치에서 4가지 방향으로 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
#                 if graph[ny][nx] == 0:
#                     graph[ny][nx] = graph[y][x] + 1
#                     queue.append([ny, nx])
#                     print("Queue ==>", queue)
#                     for g in graph:
#                         print("Graph ==>", g)
#                     print("\n")
#     # [
#     # [1, 0, 1, 1, 1], 
#     # [1, 0, 1, 0, 1], 
#     # [1, 0, 1, 1, 1], 
#     # [1, 1, 1, 0, 1], 
#     # [0, 0, 0, 0, 1]
#     # ]

#     answer = graph[-1][-1]
#     return answer


def solution(maps):
    answer = 0
    
    graph = [[0 for _ in range(len(maps))] for _ in range(len(maps[0]))]
    graph[0][0] = 1
    
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
                if graph[ny][nx] == 0:
                    dq.append([ny, nx])
                    graph[ny][nx] = graph[y][x] + 1
    
    
    answer = graph[-1][-1]
    return answer


if __name__ == "__main__":
    a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    ret = solution(a)
    print(ret)