import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
# 도시
n = int(input().strip())
# 경로수
m = int(input().strip())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().strip().split())
  graph[a].append((b, c))

start, end = map(int, input().strip().split())


def dd(start):
  q = []
  heapq.heappush(q, ( 0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dd(start)


print(distance[end])
