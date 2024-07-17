import sys

input = sys.stdin.readline
arr = []

N = int(input().strip())

for _ in range(N):
  input_data = input().strip().split()
  arr.append((input_data[0], int(input_data[1])))

result_arr = sorted(arr, key=lambda student: student[1])

for s in result_arr:
  print(s[1])
