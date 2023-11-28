import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
#01
tmp = [input().strip() for _ in range(n)]
s = [input().strip() for _ in range(m)]

dic = {}
#02
for x in tmp:
    for i in range(1,len(x)+1): dic[x[:i]] = 1
#03
cnt = 0
for i in s:
    try:
        cnt += dic[i]
    except:
        pass
print(cnt)
