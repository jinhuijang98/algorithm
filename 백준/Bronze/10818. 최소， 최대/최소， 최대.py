N = int(input())

arr = list(map(int, input().split()))

# 초기값
min_v = arr[0]
max_v = arr[0]

for i in range(N):
    # 만약 max_v 보다 arr[i]이 크다면 max_v 값에 arr[i] 값을 넣어줌
    if max_v < arr[i]:
        max_v = arr[i]
    # 처음 min_v는 무조건 0이기 때문에 이 if문을 만들어줘야함!
    # 만약 다르게 작성하고 싶다면 min_v = arr[0] 이런식으로 넣고 할 수도

    if min_v > arr[i]:
        min_v = arr[i]
print(f'{min_v} {max_v}')