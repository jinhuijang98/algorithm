# 다시

# 입력
n = int(input())

students = list(map(int,input().split()))
g = [0 for _ in range(1+n)]
# 다이나믹 프로그래밍을 이용하여

for i in range(n+1):
    ma = 0
    mi = 10001
    for j in range(i,0,-1):
        ma = max(ma,students[j-1])
        mi = min(mi,students[j-1])
        g[i] = max(g[i], ma - mi + g[j - 1])
print(g[n])