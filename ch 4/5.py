# N , M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0을 초기화
d = [[0] * m for _ in range(n)]
print(d)

# 현재 캐릭터의 X 좌표 , Y 좌표 , 방향을 입력받기
x, y, direction = map(int, input().split())

d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []

for _ in range(n):
  array.append(list(map(int, input().split())))

# 북 , 동 , 남 , 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
  global direction  # 전역변수 global
  direction -= 1
  if direction == -1:
    direction = 3


# 시물레이션 시작
count = 1
turn_time = 0  # 네 방향 모두 이미 가본칸일 경우 알기위해 (#3번 매뉴얼)
while True:
  # 1번 매뉴얼 현재 왼쪽 방향부터 차례대로 갈 곳을 정한다
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 회전한 이후 정면에 가보지 않은 칸 && 육지인칸
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue

  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인경우
  # 회전 ㄱㄱ
  else:
    turn_time += 1

  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    # 뒤로 갈 수 있다면 이동하기 (# 메뉴얼 3 한칸 뒤로 가고 1단계로 돌아간다)
    if array[nx][ny] == 0:
      x = nx
      y = ny

    # 뒤가 바다로 막혀있는 경우
    else:
      break

    turn_time = 0

# 정답 출력
print(count)