import sys

n = int(input().strip())

arr = list(map(int, input().strip().split(" ")))

arr.sort()
target = 1

for i in arr:
  if target < i:
    break
  target += i

print(target)
