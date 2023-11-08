import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [list(input().strip()) for _ in range(n)]
'''
0,0 ~ 7, 7
시작점을 .. i = 0 ~ 
1. 시작점이 B인 경우, 
2. 시작점이 W인 경우
두 가지 경우..가 있으므로

'''
# 답안을 만들어놓고 비교하기 -> 근데 더 좋은 방법이 있지 않을까..?
# print(arr[0:8][0:8])


answer = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'] for _ in range(8)]
answer1 = answer[:]
answer2 = answer[:]
for i in range(8):
    if i % 2:
        answer1[i] = answer1[i][::-1]
    else:
        answer2[i] = answer2[i][::-1]

min_cnt = 9999999999999999999999999


for i in range(n-7):
    for j in range(m-7):
        ans = []
        cnt_1 = 0
        cnt_2 = 0
        for a in range(i, i+8):
            x = []
            for b in range(j, j+8):
                x.append(arr[a][b])
            ans.append(x)
        for k in range(8):
            for l in range(8):
                if answer1[k][l] != ans[k][l]:
                    cnt_1 += 1
                elif answer2[k][l] != ans[k][l]:
                    cnt_2 += 1
        min_cnt = min(cnt_1, cnt_2, min_cnt)
print(min_cnt)
