import sys
input = sys.stdin.readline

n,m = map(int,input().split())
superior = list(map(int,input().split()))
ans = [0]*(n+1)
        
for _ in range(m):
    i,w = map(int,input().split())
    ans[i] += w
    
for i in range(2,n+1):
    ans[i] += ans[superior[i-1]]    
    
ans.pop(0)           
print(*ans)