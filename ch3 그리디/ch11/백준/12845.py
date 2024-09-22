import sys

n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
money = 0
arr.sort(reverse=True)

while (len(arr) > 1):
  money = money + arr[0] + arr[1]
  del arr[1]

print(money)
