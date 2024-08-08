import sys

n, m = map(int, input().strip().split(" "))
arr = list(map(int, input().strip().split(" ")))

count = [0] *(n+1)

result = n*(n-1) // 2  
for i in arr:
  count[i] +=1

for i in count:
  if i ==2 :
    result -=1


print(result)
