import sys
import copy

input = sys.stdin.readline

n = int(input().strip())
h = 0
result = 0
graph = []

for _ in range(n):
  graph.append(list(map(int, input().strip().split(" "))))


def dfs(x, y):

  if x < 0 or x >= n or y < 0 or y >= n:
    return False

  if graph2[x][y] == 0:
    return False

  if graph2[x][y] >= h: 
    graph2[x][y] = 0
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True

  return False

maxH =0
for i in range(0, 101):
  h = i
  result = 0
  graph2 = copy.deepcopy(graph)
  for j in range(n):
    for k in range(n):
      if dfs(j, k):
        result += 1
  # if result > h: # 여기 h 가 아니라 maxH로 새로 변수 선언을 해줘야하는데 안해줘서 틀림
  #   h = result
  if result > maxH:
    maxH = result

print(h)
