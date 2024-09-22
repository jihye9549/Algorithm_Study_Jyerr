# 내가 짠 코드
import sys

input = sys.stdin.readline
k, n = map(int, input().strip().split())
arr = []
for _ in range(k):
  arr.append(int(input().strip()))

start = 0
end = max(arr)
mid_result = 1
count_n = n

while (start <= end):
  result = 0
  mid = (start + end) // 2
  for i in arr:
    result += i // mid
  if result > n:
    start = mid + 1
  elif result < n:
    end = mid - 1
  else:
    mid_result = mid
    break

while True:
  result = 0
  for i in arr:
    result += i // mid_result
  if result == n:
    mid_result += 1
  else:
    break

print(mid_result-1)



# 수정 해서 맞춘 코드

import sys

input = sys.stdin.readline
k, n = map(int, input().strip().split())
arr = []
for _ in range(k):
    arr.append(int(input().strip()))

start = 1  # 최소 길이는 1로 수정
end = max(arr)
mid_result = 0

while start <= end:
    mid = (start + end) // 2
    result = sum(i // mid for i in arr)  
    
    if result >= n:  # N개 이상 만들 수 있는 경우
        mid_result = mid  # 가능한 최대 길이 갱신
        start = mid + 1
    else:
        end = mid - 1

print(mid_result)
