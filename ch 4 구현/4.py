input_data = input()
row = int(input_data[1])
# ord("a") => 정수 97반환
column = int(ord(input_data[0])) - int(ord("a")) + 1  # a는 1이 되고 , b는 2가 되고 ...

# 나이트가 이동할 수 있는 8가지 방향 정의
# 이동가능 횟수만 구하면 되므로 순서는 상관없다
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column +step[1]
  
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if( next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8):
    result += 1

print(result)
