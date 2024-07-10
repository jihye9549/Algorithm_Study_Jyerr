p, m = map(int, input().split())
people = []
for i in range(p):
    lv, id = input().split()
    people.append([int(lv), id])

rooms = []

for lv, id in people:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m: # 방의 전원이 다 찼으면 넘어감
            continue
        
        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10:
            flag = True # 방에 들어갔을때는 flag를 True로 했기 때문에 뒤에 if 문에 들어가지 X
            rooms[i][1].append([lv, id])
            break
            
    # 대기방에 들어 갈 수 없으면 새로운 방 생성
    if not flag:
        rooms.append([lv, [[lv, id]]])

# 방이 생성된 시간 순서로 출력
for i in range(len(rooms)):
  if len(rooms[i][1]) == m:  # 방의 전원이 다 찼으면 시작 가능
    print('Started!')
    tmp_ids = sorted(rooms[i][1], key=lambda x: x[1]) # a, b, c .. 순으로 정렬
    for j in range(m):
      print(*tmp_ids[j]) # 리스트 또는 튜플의 요소를 개별 인자로 풀어준다 ex ) [1,2,3] -> 1 2 3
  else:
    print('Waiting!')
    tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
    for j in range(len(tmp_ids)):
      print(*tmp_ids[j])