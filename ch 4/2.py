# 완전 탐색 유형 !!
n = int(input())
count = 0
for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      if ('3' in str(i) + str(j) + str(k)): # 여기가 중요 !  다 문자열로 만들어서 해당 문자열에 '3' 문자가 있는지 찾는다
        count += 1

print(count)
