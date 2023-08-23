
T = int(input())

for tc in range(1, T+1):
    # N : 수강생의 수
    # K : 과제를 제출한 사람의 수
    N, K = map(int, input().split())
    # arr : 과제를 제출한 사람의 번호
    arr = list(map(int, input().split()))
    # 1~N번까지의 번호
    student = [i+1 for i in range(N)]
    for i in range(K):
        student.remove(arr[i])
    print(f'#{tc}', end=' ')
    for x in range(len(student)):
        print(student[x], end= ' ')
    print()
