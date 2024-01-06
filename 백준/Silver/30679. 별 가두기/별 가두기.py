# 30679 별 가두기
'''
n x m 크기의 격자. 양의 정수
1. 첫번째 열의 원하는 칸에 별을 올려둔다.
2. 별 이동
    1. 별은 바라보고 있는 방향으로, 별이 놓인 칸에 적힌 수만큼 이동
    2. 별이 바라보는 방향이 시계 방향으로 90도 돌아감
별은 처음에 오른쪽을 바라보고 있으며, 별이 격자 밖으로 나가지 않고
위 과정이 무한히 반복된다면 별을 성공적으로 가둔것.
하지만 중간에 별이 격자 밖으로 나가게 된다면 별을 가두는 데 실패패

처음에 별을 어느 칸에 올려놔야 별을 가둘 수 있을까?
'''

import sys
input = sys.stdin.readline

# n : 세로 , m : 가로
n, m = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(n)]

'''
첫째 줄에는 별을 가두기 위해 처음 올려둘 수 있는 칸의 개수
별을 가두기 위해 처음에 올려둘 수 있는 칸들이 몇 번째 행에 있는지 
공백을 사이에 두고 오름차순 출력. 존재하지 않으면 출력 x

n번 반복
'''

# 방향 -> 4방향
# 거리 -> arr[x][y]
# 만약 방문했던 곳의 방향이 같으면 -> 출력
# 만약 n,m을 넘어가면 0 출력

result = []
for i in range(n):
    x = i
    y = 0
    # 시작점은 x, y
    visited = [[0]*m for _ in range(n)]
    d = 0
    visited[x][y] = (arr[x][y], d)
    # print(visited)
    while True:
        # 시작점 x, y
        nx = x
        ny = y
        d = d % 4
        if d % 4 == 0:
            ny += arr[x][y]
        elif d % 4 == 1:
            nx += arr[x][y]
        elif d % 4 == 2:
            ny -= arr[x][y]
        else:
            nx -= arr[x][y]
        if 0 <= nx < n and 0 <= ny < m:
            d += 1
            d = d % 4
            if visited[nx][ny] != (arr[nx][ny], d):
                visited[nx][ny] = (arr[nx][ny], d)
                x = nx
                y = ny
            else:
                result.append(i+1)
                break
        else:
            break
print(len(result))
if result:
    print(*result)




