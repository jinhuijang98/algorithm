# 10472 십자뒤집기

import sys
input = sys.stdin.readline
from collections import deque
import copy

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
'''
 "*"은 검은색을 뜻하며 "."은 흰색을 뜻한다.

'''

# print(q)
t = int(input().strip())

def convert_board(board, x, y):
    ret = copy.deepcopy(board)

    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            if ret[nx][ny] == '*':
                ret[nx][ny] = '.'
            else:
                ret[nx][ny] = '*'
    return ret


def convert_to_binary(board):
    binary_str = ''

    for x in range(3):
        for y in range(3):
            binary_str += '0' if board[x][y] == '.' else '1'

    return int(binary_str, 2)

def bfs(goal):
    time = 0
    init_board = [['.', '.', '.'] for _ in range(3)]
    visit = [0] * 1000

    q = deque([init_board])
    visit[convert_to_binary(init_board)] = 1

    while q:
        loop = len(q)
        for _ in range(loop):
            board = q.popleft()
            if board == goal:
                return time

            for row in range(3):
                for col in range(3):
                    next_board = convert_board(board, row, col)
                    binary_code = convert_to_binary(next_board)

                    if not visit[binary_code]:
                        q.append(next_board)
                        visit[binary_code] = 1

        time += 1

for _ in range(t):
    arr = [list(input().strip()) for _ in range(3)]
    time = bfs(arr)
    answer = time
    print(answer)