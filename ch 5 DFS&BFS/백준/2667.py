import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input().strip())
field = []
result = []
count = 1
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for _ in range(n):
  field.append(list(map(int, input().strip())))


def dfs(x, y, count):
  field[x][y] = 0
  for dx, dy in d:
    X, Y = x + dx, y + dy
    if (0 <= X < n) and (0 <= Y < n) and field[X][Y] == 1:
      count = dfs(X, Y, count + 1)
  return count


for i in range(n):
  for j in range(n):
    if field[i][j] == 1:
      result.append(dfs(i, j, count))
      count = 1

print(len(result))
result.sort()
for i in result:
  print(i)
