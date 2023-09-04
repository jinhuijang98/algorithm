import sys
input = sys.stdin.readline

#
# def bfs(s):
#     q = []
#     q.append(s)
#     visited = [0] * n
#     while q:
#         x = q.pop(0)
#         for i in range(2):
#

T = int(input().strip())

for _ in range(T):
    # n : 통나무의 개수
    # arr : 각 통나무의 높이 배열
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    # 홀수와 짝수 인덱스 순서대로 나누기
    n1_list = []
    n2_list = []
    for i in range(n):
        if (i+1) % 2:
            n1_list.append(arr[i])
        else:
            n2_list.append(arr[i])
    n2_list.sort(reverse=True)
    # 규칙 찾아서 최종 배열 형성
    fin_list = n1_list + n2_list
    level = 0
    for i in range(n-1):
        # if i == 0:
        #     level = max(abs(fin_list[i] - fin_list[i+1]), abs(fin_list[i]-fin_list[-1]))
        # else:
        # n-1까지 돌면서 최댓값 갱신
        if level < max(abs(fin_list[i] - fin_list[i+1]), abs(fin_list[i] - fin_list[i-1])):
            level = max(abs(fin_list[i] - fin_list[i+1]), abs(fin_list[i] - fin_list[i-1]))
    print(level)