# bobble sorting 구현
def BubbleSort(a, N):
    # i는 구간의 끝을 의미
    for i in range(N-1, 0, -1):
        # j는 비교할 원격 원소 
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(BubbleSort(arr, 10)[-3])
