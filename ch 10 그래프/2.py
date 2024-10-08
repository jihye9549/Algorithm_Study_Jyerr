import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

parent = [0] * (n + 1)  # 부모 테이블 초기화

# 부모 테이블상에서 , 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
  parent[i] = i


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면 , 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


for _ in range(m):
  cal, a, b = map(int, input().strip().split())
  if (cal == 0):
    union_parent(parent, a, b)

  else:
    if parent[a] == parent[b]:
      print("yes")
    else:
      print("no")
