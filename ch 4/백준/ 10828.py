import sys

n = int(sys.stdin.readline())
arr = list()
top = -1

for _ in range(n):
  ha = sys.stdin.readline().strip()
  if "push" in ha:
    name, num = ha.split()
    arr.append(num)
    top += 1

  if "top" == ha:
    if (top == -1):
      print(-1)
    else:
      print(arr[top])

  if "pop" == ha:
    if (top == -1):
      print(-1)
    else:
      print(arr[len(arr) - 1])
      arr.pop()
      top -= 1

  if "size" == ha:
    print(len(arr))

  if "empty" == ha:
    if (top == -1):
      print(1)
    else:
      print(0)
