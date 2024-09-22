import sys

input = sys.stdin.readline
n, k = input().strip().split()

arrA = list(map(int,input().strip()))
arrB = list(map(int,input().strip()))

arrA.sort()
arrB.sort(reverse=True)


for i in range(k):
    if arrA[i] < arrB[i]: 
      arrA[i] , arrB[i] = arrB[i], arrA[i]
    else:
      break
print(sum(arrA))