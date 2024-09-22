import sys
import heapq


input = sys.stdin.readline

n = int(input().strip())
heap = []

arr = list(map(int, input().strip().split()))
for num in arr:
  heapq.heappush(heap, num)

for _ in range(n - 1):
  arr = list(map(int, input().strip().split()))
  for num in arr:
    if heap[0] < num:
      heapq.heappop(heap)
      heapq.heappush(heap, num)

print(heap[0])


# https://naroforme.tistory.com/entry/%EB%B0%B1%EC%A4%80-2075%EB%B2%88-N%EB%B2%88%EC%A7%B8-%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 메모리 제한이 뜰경우 2차원배열이나 튜플을 이용 X => 최소힙 구조에서 조건문을 사용하여 최소한의 메모리를 사용해라