import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x, y, n, m):
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    # 상하좌우의 위치도 모두 재귀적으로 호출
    #  재귀 호출 순서는 탐색 순서에만 영향을 미치며, 전체 연결된 컴포넌트를 탐색하는 결과에는 영향을 미치지 X
    dfs(x - 1, y, n, m)
    dfs(x + 1, y, n, m)
    dfs(x, y - 1, n, m)
    dfs(x, y + 1, n, m)
    return True
  return False


t = int(input().strip())

for _ in range(t):
  result = 0
  m, n, k = map(int, input().strip().split())
  graph = [[0] * m for _ in range(n)]  # n이 세로, m이 가로
  #[0] * m 이 길이가 m인 리스트를 만들고 모두 0으로 초기화
  for _ in range(k):
    x, y = map(int, input().strip().split())
    graph[y][x] = 1  # 입력 좌표는 (가로, 세로) 순서로 주어짐

  for i in range(n):
    for j in range(m):
      if dfs(i, j, n, m): # True 일때만 카운트
        result += 1

  print(result)
