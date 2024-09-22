# 이진탐색으로 푼 나의 코드

import sys

input = sys.stdin.readline
n = int(input().strip())
arrN = list(map(int, input().strip().split()))
m =  int(input().strip())
arrM = list(map(int, input().strip().split()))


arrN.sort()


def binary_search(arr, target , start , end) :
  while(start <=end):
    mid = (start+end )//2
    if arr[mid] == target:
      return True
    else:
      if(arr[mid] > target):
        end = mid -1
      else:
        start = mid +1
  return False
  
for i in arrM :
  if(binary_search(arrN, i , 0 , n-1)):
    print("yes",end=" ")
  else:
    print("no",end=" ")
    
 
  
  
  