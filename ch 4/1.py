# N을 입력받기
n = int (input())
x , y = 1 , 1
plans = input().split()


# L R U D 에 따른 이동 방향

dx = [0 ,0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']


# 이동 계획을 하나씩 확인
for plan in plans :
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      # 오른쪽 , 왼쪽 으로 이동하면 y의 값이 변화함!!;; 
      nx = x + dx[i]
      ny = y + dy[i]
    


    # 공간을 벗아나는 경우 무시
    if(nx <1 or ny <1 or nx >n or ny >n ):
      continue
    # 이동 수행
    x = nx
    y = ny

print(x, y)

