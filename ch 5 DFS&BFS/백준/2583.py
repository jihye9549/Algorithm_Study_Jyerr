import sys

sys.setrecursionlimit(10000)

M, N, K = map(int, sys.stdin.readline().split())

field = [[0 for _ in range(N)] for _ in range(M)]  #M이 세로 N이 가로

for _ in range(K):
  X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
  for Y in range(Y1, Y2):  # 사이의 범위를 1로 만들어준다
    for X in range(X1, X2):
      field[Y][X] = 1


def dfs(x, y, count):
  field[y][x] = 1
  for dx, dy in d:
    X, Y = x + dx, y + dy
    if (0 <= X < N) and (0 <= Y < M) and field[Y][X] == 0:
      count = dfs(X, Y, count + 1)

  return count


area = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# N*M 직사각형을 전부 돌면서, 분리된 영역(리스트에서 0이 할당된 값)을 찾고, DFS 함수를 호출
for Y in range(M):
  for X in range(N):
    if field[Y][X] == 0:
      area.append(dfs(X, Y, count=1))

print(len(area))
print(*sorted(area))
