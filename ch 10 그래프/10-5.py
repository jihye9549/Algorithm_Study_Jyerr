# 크루스칼 알고리즘 (= 최소 신장 트리 알고리즘)
# ✨ 신장트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# ✨ 최소신장트리 = 신장트리들중 가장 최소한의 비용을 가지는 트리
# (신장 트리에 포함되는 [ "간선의 개수" = "노드의 개수" -1] )


# 노드의 개수와 간선의 개수 입력받기
v , e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges= []
result = 0

# 부모 테이블상에서 , 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
  # 루트 노드가 아니라면 , 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
    


# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a < b :
    parent[b] = a
  else:
    parent[a] = b



# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
  a,b, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해서 튜플의 첫 번쨰 원소를 비용으로 설정
  edges.append((cost,a,b))
  
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for  edge in edges:
  cost,a,b=  edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent,a) !=  find_parent(parent,b) :
    union_parent(parent,a,b)
    result+=cost

print(result)