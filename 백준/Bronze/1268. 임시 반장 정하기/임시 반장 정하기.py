import sys
input = sys.stdin.readline

# n : 학생 수
n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
# 반 리스트
max_v = 0   # 같은 반이 최대 몇명과?
x = 0    # 모두 같은 반이 되지 않을 경우
for i in range(n):
    ca = [0] * n   # 1번 학생이 2, ... ,n번학생과 같은 반이 된 횟수 저장
    for j in range(5):      # 열로 탐색
        sa = arr[i][j]    # 반 저장
        for k in range(n):  # n번씩 돌면서
            if i != k and sa == arr[k][j]:    # 만약 save값과 같다면
                ca[k] = 1      # 같은반이 됐다는 의미이므로 1로 값 변경
    cnt = 0     # 다른 학생과 총 몇번 같은 반이 됐는지 횟수 계산
    for l in range(n):
        if ca[l] != 0:
            cnt += 1    # 0이 아니라면 같은 반이 된 적 있다는 의미이므로
    if max_v < cnt:     # 최종 가장 큰 값을 max_v에 저장/등호 넣으면 뒤의 값이 되므로 등호 제거
        max_v = cnt
        x = i           # 인덱스 저장
print(x+1)
