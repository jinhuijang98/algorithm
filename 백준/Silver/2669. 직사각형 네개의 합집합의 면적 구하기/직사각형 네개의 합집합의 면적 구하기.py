# 직사각형 위치를 나타내는 2차원 배열 만들기
arr = [[0]*4 for _ in range(4)]
# 전체 직사각형 좌표
nemo = [[0]*100 for _ in range(100)]
for i in range(4):
    arr[i] = list(map(int, input().split()))

# print(arr)
for i in range(4):
    start_r = arr[i][0]
    start_c = arr[i][1]
    fin_r = arr[i][2]
    fin_c = arr[i][3]
    for j in range(start_r, fin_r):
        for k in range(start_c, fin_c):
            nemo[j][k] = 1

# 최종 결과값
total = 0
for i in range(100):
    for j in range(100):
        if nemo[i][j] == 1:
            total += 1

print(total)