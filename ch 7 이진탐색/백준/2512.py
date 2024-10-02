import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split(" ")))
arr.sort()
money = int(input())

start =1
mid =0
end = arr[n-1]
ans=0
sum =0


for i in range(n):
    sum += arr[i]
if sum <= money:
    print(arr[n-1])
else:
    while(end >=start):
        sum = 0
        mid = (end + start)//2
        for i in range(n):
            if (arr[i]<mid):
                sum+=arr[i]
            else:
                sum+=mid
        if sum <= money:
            ans = mid
            start = mid+1
        elif sum > money:
            end = mid-1

        
    print(ans)
            
    
