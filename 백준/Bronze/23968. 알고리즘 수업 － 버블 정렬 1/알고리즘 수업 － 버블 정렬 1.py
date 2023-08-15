import sys
input = sys.stdin.readline

# 버블 정렬 함수
def bubblesort(arr, K, N):
    cnt = 0
    # new_list = []
    for i in range(N-1, -1, -1):
         for j in range(i):
            if arr[j] > arr[j+1]:
                cnt += 1
                if cnt == K:
                    # new_list.append(arr[j+1])
                    # new_list.append(arr[j])
                    return [str(arr[j+1]), str(arr[j])]
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return -1

a, k = map(int, input().split())
arr = list(map(int, input().split()))
x = bubblesort(arr, k, a)
if x != -1:
    print(' '.join(x))
else:
    print(-1)