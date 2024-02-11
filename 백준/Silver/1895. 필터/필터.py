R, C = map(int, input().split())
 
Filter = []
for r in range(R) :
    Filter.append(list(map(int,input().split())))
 
T = int(input())
J = []
 
for r in range(R-3+1) :
    for c in range(C-3+1) :
        median = []
        for i in range(r, r+3) :
            for j in range(c, c+3) :
                median.append(Filter[i][j])
 
        median.sort()    
        J.append(median[4])
 
cnt = 0
for k in J:
    if k > T or k == T :
        cnt += 1
 
print(cnt)