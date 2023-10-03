def DFS(L,total):
    global s
    if total>s:
        return
    if L==k:
        if 0<total<=s:
            ch[total]=1
    else:
        DFS(L+1,total+w[L])
        DFS(L+1,total-w[L])
        DFS(L+1,total)

k=int(input())
w=list(map(int,input().split()))
s=sum(w)
ch=[0]*(s+1)
DFS(0,0)
cnt=0
for x in ch:
    if x==0:
        cnt+=1
print(cnt-1)