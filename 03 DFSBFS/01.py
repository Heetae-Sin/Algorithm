def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    # 현재좌표가 방문처리가 안되었을 때
    if graph[x][y] == 0:
        
        # 방문처리를 하고
        graph[x][y] = 1
        
        # 인접한 노드를 모두 방문처리 한다.
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        
        return True
    return False


# 입력
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1