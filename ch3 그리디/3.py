n, m = map(int, input().split())
lis = []

for _ in range(n):
  data = list(map(int, input().split()))
  data.sort()
  lis.append(data[0])

lis.sort()
print(lis[-1])


# min() 과 max() 사용 가능
# 답지
n, m = map(int, input().split())
result = 0

for _ in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result,min_value)


print(result)