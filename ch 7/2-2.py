# 계수 정렬 활용 답안

n  = int(input())
array = [0] * 1000000

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] =1

# M 입력받기
m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청환 부품 번호를 하나씩 확인
for i in x :
  # 해당 부품이 존재하는지 확인
  if array[i] == 1 :
    print("yes",end =" ")
  else:
    print("no",end=" ")
