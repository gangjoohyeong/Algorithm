from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    visited = [ [ False for _ in range(m) ]  for _ in range(n) ]
    survives = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                queue = deque([(i, j)])
                survive = int(maps[i][j])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            survive += int(maps[nx][ny])
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                survives.append(survive)
                
    if not survives:
        return [-1]
    else:
        return sorted(survives)
                            
                        
    