import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

arr = []

result = 0

for _ in range(n):
  heapq.heappush(arr, int(input()))

while len(arr) !=1:
  a = heapq.heappop(arr)
  b = heapq.heappop(arr)
  result += a+b
  heapq.heappush(arr, a+b)
 

print(result)
