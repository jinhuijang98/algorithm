n=int(input()) #도시의 개수
km=list(map(int,input().split()))#도로의 길이
price=list(map(int,input().split()))#가격

minPrice=price[0]
total=0

for i in range(n-1):
    if minPrice>price[i]:
        minPrice=price[i]

    total+=(minPrice*km[i])
print(total)