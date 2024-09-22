import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())

arrH = list(map(int, input().strip().split()))

start = 0
end = max(arrH)

# 이진 탐색 수행(반복적)
result = 0
while (start <= end):

  total = 0
  mid = (start + end) // 2

  # 잘랐을 때의 떡의 양 계산
  for x in arrH:
    if (x > mid):
      total += x - mid

  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if (total < m):
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid  # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
    start = mid + 1

print(result)
