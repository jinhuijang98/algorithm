# 카운팅 정렬을 하는 함수
def counting_sort(arr):
    counts = [0] * 101 # 1~100까지의 수가 몇개씩 있는지 담을 리스트
    # 0번째는 사용하지 않고 그니까 인덱스를 사용하려고
    temp = [0] * 100 # 매개변수 arr을 정렬한 배열을 담을 리스트
    # 1 ~ 100까지의 수가 몇개씩 있는지 카운팅
    for i in arr:
         counts[i] += 1
    for i in range(1, 101):
        counts[i] += counts[i - 1]
    # 매개변수 arr의 뒤에서부터 탐색하며
    for j in range(99, -1, -1):
        counts[arr[j]] -= 1
        temp[counts[arr[j]]] = arr[j]
    return temp


# def counting_sort(arr):
#     counts = [0] * 101  # 1 ~ 100까지의 수가 몇개씩 있는지 담을 리스트
#     temp = [0] * 100    # 매개변수 arr을 정렬한 배열을 담을 리스트
#     # 1 ~ 100까지의 수가 몇개씩 있는지 카운팅
#     for i in arr:
#         counts[i] += 1
#     # 카운팅 배열의 index 값을 구하기 위해 앞에 값부터 더하기
#     for i in range(1, 101):
#         counts[i] += counts[i - 1]
#     # 매개변수 arr의 뒤에서 부터 탐색하며 구해놓은 index에 맞춰서 정렬
#     for i in range(99, -1, -1):
#         counts[arr[i]] -= 1
#         temp[counts[arr[i]]] = arr[i]
#     # 정렬한 배열을 반환
#     return temp

for tc in range(1, 11):
    # 덤프 횟수
    N = int(input())
    arr = list(map(int, input().split()))
    # 처음 정렬하고 시작
    arr = counting_sort(arr)
    for i in range(N):
        # if arr[0]<= arr[-1]:
            arr[0]+=1
            arr[-1]-=1
            arr = counting_sort(arr) # 덤프 후 다시 정렬 !!!!
        # else:
    rlt = arr[-1] - arr[0]

    print(f'#{tc} {rlt}')