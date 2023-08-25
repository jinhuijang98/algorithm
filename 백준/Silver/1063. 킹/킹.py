import sys
input = sys.stdin.readline

# k : 킹의 위치
# s : 돌의 위치
# n : 움직이는 횟수
k, s, n = input().strip().split()
n = int(n)
# 어떻게 움직이는지를 담은 배열
arr = []
for i in range(n):
    x = input().strip()
    arr.append(x)
# print(arr)

# 알파벳은 열, 숫자는 행
# 체스판 8x8
chess = [[0]*8 for _ in range(8)]
# print(chess)
# 행과 열에 대응 되는 값 변경
col = {'A' : 0, 'B' : 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
row = {8 : 0, 7 : 1, 6: 2, 5: 3, 4 : 4, 3 : 5, 2 : 6, 1 : 7}
# col은 -1

# 킹의 위치와 돌의 위치 chess에 표시
kx = row[int(k[1])]
ky = col[k[0]]

sx = row[int(s[1])]
sy = col[s[0]]

# 킹의 위치 k로 표시
chess[kx][ky] = 'k'
# 돌의 위치 s로 표시
chess[sx][sy] = 's'

# print(chess)
  # 행  열
# R = [0, 1]
# L = [0, -1]
# B = [1, 0]
# T = [-1, 0]
# RT = [-1, 1]
# LT = [-1, -1]
# RB = [1, 1]
# LB = [1, -1]

# 현재 킹의 위치 = kx, ky
# 움직인 후의 킹의 위치 = nkx, nky
# 현재 돌의 위치 = sx, sy
# 움직인 후의 돌의 위치 = nsx, nsy
nkx = kx
nky = ky
nsx = sx
nsy = sy
for i in range(n):
    if 'R' == arr[i]:
        nky = ky + 1
    elif 'L' == arr[i]:
        nky = ky - 1
    elif 'B' == arr[i]:
        nkx = kx + 1
    elif 'T' == arr[i]:
        nkx = kx - 1
    elif 'RT' == arr[i]:
        nkx = kx - 1
        nky = ky + 1
    elif 'LT' == arr[i]:
        nkx = kx -1
        nky = ky -1
    elif 'RB' == arr[i]:
        nkx = kx + 1
        nky = ky + 1
    else:   # 'LB'
        nkx = kx + 1
        nky = ky - 1
    # 움직이려고 하는 값이 범위 안에 있으면서
    if 0 <= nkx < 8 and 0 <= nky < 8:
        # 킹이 움직이려고 하는 자리에 돌이 없다면
        if chess[nkx][nky] == 0:
            chess[kx][ky] = 0
            chess[nkx][nky] = 'k'
            kx = nkx
            ky = nky
        # 킹이 움직이려고 하는 자리에 돌이 있다면
        else:
            if 'R' == arr[i]:
                nsy = sy + 1
            elif 'L' == arr[i]:
                nsy = sy - 1
            elif 'B' == arr[i]:
                nsx = sx + 1
            elif 'T' == arr[i]:
                nsx = sx - 1
            elif 'RT' == arr[i]:
                nsx = sx - 1
                nsy = sy + 1
            elif 'LT' == arr[i]:
                nsx = sx - 1
                nsy = sy - 1
            elif 'RB' == arr[i]:
                nsx = sx + 1
                nsy = sy + 1
            else:  # 'LB'
                nsx = sx + 1
                nsy = sy - 1
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                chess[sx][sy] = 0
                chess[nsx][nsy] = 's'
                chess[kx][ky] = 0
                chess[nkx][nky] = 'k'
                kx = nkx
                ky = nky
                sx = nsx
                sy = nsy
            else:
                nkx = kx
                nky = ky
                nsx = sx
                nsy = sy
    # 움직이려고 하는 값이 범위를 벗어났다면 nkx, nky 초기화하고 다음으로 넘어감
    else:
        nkx = kx
        nky = ky
    # print(chess)
    # 행, 열
# print(nkx, nky)
# print(nsx, nsy)
# kx = str(kx + 1)
# sx = str(sx + 1)
# dict을 map으로 key와 value 바꾸기
new_col = dict(map(reversed, col.items()))
new_row = dict(map(reversed, row.items()))
# new_col[ky]
print(new_col[ky]+str(new_row[kx]))
print(new_col[sy]+str(new_row[sx]))