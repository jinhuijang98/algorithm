'''
영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.


'''

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
'''
. : 빈칸
X : 경비원이 있는 칸
'''
'''
행 조회
열 조회 

'''

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            col[j] = 1

cnt_row = 0
cnt_col = 0
for i in range(n):
    if row[i] == 0:
        cnt_row += 1
for j in range(m):
    if col[j] == 0:
        cnt_col += 1


print(max(cnt_row, cnt_col))
