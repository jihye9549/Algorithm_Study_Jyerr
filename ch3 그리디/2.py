n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
count = 0

while (m > 0):
  for _ in range(k):
    count += data[-1]
    m -= 1
  count += data[-2]
  m -= 1
  print(count)

print(count)
