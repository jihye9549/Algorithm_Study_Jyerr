# 완전탐색
import sys

n = int(input().strip())
arr = []

for _ in range(n):
  arr.append(list(map(int , input().strip().split(" "))))

ans =0

def count_candy():
  row_cnt , col_cnt , row_max ,col_max = 1, 1, -1e9 ,-1e9

  # 행 계산
  for i in range(n):
    for j in range(n-1):
      if arr[i][j] ==  arr[i][j+1]:
        row_cnt +=1
      else:
        row_cnt 1
      row_max = max(row_cnt , row_max)
    row_cnt =1
    

  # 열 계산
  for i in range(n):
    for j in range(n-1):
      if arr[i][j] ==  arr[i+1][j]:
        col_cnt +=1
      else:
        col_cnt 1
      col_max = max(col_cnt,col_max)
    col_cnt = 1

  answer = max(row_max,col_max)
  return answer



# 상,하,좌,우 방향
steps=[[0,1],[0,-1],[-1,0],[1,0]]



# 하나씩 살펴보며
for i in range(n):
  for j in range(n):
    for k in range(4):
      nx = i + steps[k][0]
      ny = j + steps[k][1]

      if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue
        
      # 인접한 두 칸이 다른 색의 사탕이라면
      if arr[i][j] != arr[nx][ny]:
        arr[nx][ny] ,arr[i][j] =   arr[i][j] , arr[nx][ny]

        # 이전의 사탕 개수와 비교하며 최댓값 계산
        ans = max(ans , count_candy)
        arr[i][j] , arr[nx][ny] = arr[nx][ny] ,arr[i][j] 


print(ans)
      
      
      