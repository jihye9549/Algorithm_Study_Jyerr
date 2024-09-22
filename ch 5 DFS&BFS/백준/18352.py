import sys
from collections import deque

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

n, m, k, x = map(int, input().strip().split(" "))
graph = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().strip().split(" "))
  graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정


def bfs(x):
  queue = deque()
  queue.append(x)


# 너비 우선 탐색 수행
q = deque()
q.append(x)
while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든도시를 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
