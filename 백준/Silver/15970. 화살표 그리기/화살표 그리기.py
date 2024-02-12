##배열
n=int(input())
arr = [[]for _ in range(n)]
for _ in range(n):
    a,b = map(int,input().split())
    arr[b-1].append(a)
res = 0
for i in arr:
    i.sort()
    if len(i) <= 1:continue
    res += abs(i[0]-i[1])+abs(i[-1]-i[-2])
    for j in range(1,len(i)-1):
        res += min(abs(i[j]-i[j-1]),abs(i[j]-i[j+1]))
print(res)