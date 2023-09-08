leng = int(input())
red11 = list(map(int, input().split()))
blue11 = list(map(int, input().strip().split()))
yel11 = list(map(int, input().strip().split()))
col = []

col.append(red11)
col.append(blue11)
col.append(yel11)
# print(col)
'''
1. RED의 중간점으로 자르기
2. 중간점 기준으로 대칭이동
    1. 중간점이 현재 길이의 절반의 왼쪽인지 오른쪽인지에 따라 대칭이동하는 숫자가 달라짐
3. max(전체길이 - 노란색 중간점, 노란색 중간점 - 파란색 중간점) = 최종 길이

'''
# 길이와 이전 중간점의 초기값
# length = leng
# 이전 길이
ex_length = leng
# ex_mid = 0
left = 0
right = leng
for i in range(3):
    # 만약 두개의 위치가 같다면 그냥 넘어감
    if col[i][0] == col[i][1]:
        continue
    # 같지 않다면 => 중간점과 길이 바꾸기
    else:
        # 1. 중간점 찾기
        mid = (col[i][0] + col[i][1]) / 2
        # 2. 중간점 기준으로 먼저 길이 자르기
        if mid <= ((left+right) / 2):
            left = mid
        else:
            right = mid
        for j in range(i, 3):
            for k in range(2):
                if col[j][k] < left:
                    col[j][k] = 2 * left - col[j][k]
                elif col[j][k] > right:
                    col[j][k] = 2 * right - col[j][k]

print(f'{right-left:.1f}')


