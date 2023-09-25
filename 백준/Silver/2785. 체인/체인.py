n = int(input())
stg = sorted(list(map(int,input().split())))
ttl = len(stg)
rst = 0
for i in stg:
    if ttl<=1:
        break
    if i>=ttl-1:
        rst+=ttl-1
        break
    elif i == 1:
        ttl-=2
        rst+=1
    else:
        for j in range(i-1):
            ttl-=1
            rst+=1
        ttl-=2
        rst+=1
print(rst)