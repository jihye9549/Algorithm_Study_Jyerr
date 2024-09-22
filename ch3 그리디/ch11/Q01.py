import sys

input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int, input().strip().split(" ")))

arr.sort()
count =0
result =0

for i in arr: # 공포도를 낮은 것부터 하나씩 확인하여
  count = count +1 # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1
    count = 0

print(result)
    
  
  

  