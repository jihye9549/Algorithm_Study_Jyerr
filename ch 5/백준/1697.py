#bfs
from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 수빈이의 위치, 동생의 위치


def bfs(n, k):
  visited = [-1] * 100001  #길이가 100001인 리스트 생성.  0 ~  100000 모두 -1 로 초기화
  visited[n] = 0
  q = deque([n])  # 큐 생성 + n 넣음

  while q:  # 큐가 빌떄까지
    cur = q.popleft()

    if cur == k:
      return visited[cur]

    # 동생의 위치에 도달할 때 까지, 3가지의 이동 경우를 확인 (x + 1, x - 1, x * 2)
    #  cur + 1, cur - 1, cur * 2의 세 가지 값을 차례대로 next 변수에 할당하며 루프를 실행
    for next in (cur + 1, cur - 1, cur * 2):
      if 0 <= next <= 100000 and visited[next] == -1: 
        if next == cur * 2:
          visited[next] = visited[cur] + 1
          q.appendleft(next)  # appendleft()로 순간이동을 먼저 탐색
        else:
          visited[next] = visited[cur] + 1  # 걸어서 이동은 1초 소요
          q.append(next)


print(bfs(n, k))
