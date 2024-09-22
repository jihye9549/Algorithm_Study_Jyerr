n = int(input())
m = list( map(int, input().split(' ')))
 
for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i-1])
    
print(max(m))

#문제 풀이의 핵심은 "이전까지 모든 숫자의 합 중 최대값"을 그때그때 기록하는 것
#데이터의 시작점인 0번 인덱스는 이전까지의 합이 0 자신 자체이기 때문에 아무런 필요가 없다..
#https://data-marketing-bk.tistory.com/entry/%EB%B0%B1%EC%A4%80-1912%EB%B2%88-%EC%97%B0%EC%86%8D%ED%95%A9%ED%8C%8C%EC%9D%B4%EC%8D%AC