from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 밖인 경우 건너 뜀
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            # 괴물이 있는 곳은 건너 뜀
            if graph[nx][ny] == 0:
                continue
            
            # 갈 수 있는경우 현재 값에 + 1 하여 출발점 부터 거리 표시
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        
    return graph[N-1][M-1]

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 이동방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))