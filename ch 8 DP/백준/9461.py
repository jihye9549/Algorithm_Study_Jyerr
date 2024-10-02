import sys

input = sys.stdin.readline

n = int(input().strip())

d = [0] * 102
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

for i in range(6, 102):
  d[i] = d[i - 5] + d[i - 1]

for _ in range(n):
  k = int(input().strip())
  print(d[k])