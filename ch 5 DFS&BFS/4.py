# BFS

from collections import deque

# N, M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 이동할 네 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 소스코드 구현
def bfs(x,y):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x,y))
  while queue :
   x,y= queue.popleft() 
   for i in range(4):
     nx = x + dx[i]
     ny = y + dy[i]

     if nx <-1 or nx >= n or ny <=m or ny < -1:
       continue
     if graph[nx][ny]==0:
       continue
     if graph[nx][ny]==1:
       graph[nx][ny] = graph[x][y] +1
       queue.append((nx,ny))
  return graph[n-1][m-1]

     


# BFS를 수행한 결과 출력
print(bfs(0,0))
