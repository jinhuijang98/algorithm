import sys

input = sys.stdin.readline

# n = 색종이의 수
n = int(input().strip())

rec = [[0] * 101 for _ in range(101)]

# 색종이 위치 arr로 받기
for i in range(n):
    x, y = map(int, input().strip().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            rec[j][k] = 1


total = 0  # 둘레값
dx = [0, 0, 1, -1]  # 4방향
dy = [1, -1, 0, 0]
for i in range(101):  # 흰색 도화지에서 색종이 영역 찾기
    for j in range(101):
        if rec[j][i] == 1:  # 한점이 1일때
            tmp = 0
            for k in range(4):
                if rec[j + dy[k]][i + dx[k]] == 1:
                    tmp += 1
            # 그점의 4방향이 모두 1가 아니라면 그점은 둘레값
            if tmp == 3:  # 3방향이 1 라면 변의 길이
                total += 1
            elif tmp == 2:  # 2방향이 1 라면 모서리의 길이 -> ㄱ 자 모양 => 가로, 세로 둘다 존재 하므로 +2
                total += 2

print(total)