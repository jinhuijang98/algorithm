# 1388 바닥 장식

'''
기훈이의 바닥 장식을 디자인. 몇 개의 나무판자가 필요?
나무 판자는 크기 1의 너비. 양수의 길이.
기훈이의 방은 직사각형, 방 안에는 벽과 평행한 모양의 정사각형

제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자

방바닥 장식하는데 필요한 나무 판자의 개수?

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [list(input().strip()) for _ in range(n)]

result = 0
# 행 단위 탐색
for i in range(n):
    check = ''
    for j in range(m):
        if arr[i][j] == '|':
            check = arr[i][j]
            continue
        # arr[i][j] == '-'
        else:
            if check == '-':
                continue
            else:
                check = arr[i][j]
                result += 1

# 열 단위 탐색
for j in range(m):
    check = ''
    for i in range(n):
        if arr[i][j] == '-':
            check = arr[i][j]
            continue
        else:
            if check == '|':
                continue
            else:
                check = arr[i][j]
                result += 1

print(result)


