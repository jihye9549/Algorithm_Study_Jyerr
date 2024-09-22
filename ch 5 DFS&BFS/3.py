# DFS

n , m = map(int. input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문

def dfs(x,y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x < 0 or y <0 or x >=n or y>=m:
    return False
  if graph[x][y] == 0 :
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i,j) == True:
      result+=1