n, m = map(int, input().split())
count = 0
while (n > 1):
  if (n % m == 0):
    n = n / m
  else:
    n = n - 1
  count = count + 1

print(count)

