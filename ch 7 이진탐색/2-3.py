# set() 함수를 활용한 답안
n = int(input())


# ✨ set 자료형 특징 {1,2,3}
# 1️⃣ 중복을 허용하지 않는다.
# 2️⃣ 순서가 없다.
# ==> 단순히 특정한 데이터가 존재하는지 검사할때 매우 효과적으로 사용할 수 있다


# 가게에 있는 전체 부품 번호를 입력받아서 집합 (set) 자료형에 기록
array = set(map(int,input().split()))

# M을 입력받기
m = int(input())
x = list(map(int , input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  if i in array:
    print("yes",end=" ")
  else :
    print("no",end=" ")