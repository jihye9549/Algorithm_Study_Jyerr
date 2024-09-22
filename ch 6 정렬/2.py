import sys

input = sys.stdin.readline
arr = []

N = int(input().strip())

for _ in range(N):
  arr.append(int(input().strip()))

arr.sort(reverse=True)
print(*arr)
