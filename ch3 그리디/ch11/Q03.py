import sys

input = sys.stdin.readline
data = input().strip()
count0 = 0
count1 = 0

if data[0] == '1':
  count0 +=1

if data[0] == '0':
  count1+=1

# 두번쨰 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
  if data[i] != data[i+1]:
    # 다음 수에서 1로 바뀌는 경우
    if data[i+1] == "1":
      count0 += 1
    else:
      count1 += 1
  

  
  