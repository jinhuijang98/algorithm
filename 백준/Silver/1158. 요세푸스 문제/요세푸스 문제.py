N, K = map(int, input().split())

arr = [i for i in range(1, N+1)] # 맨 처음 원에 앉아 있는 사람들
pointer = 0 # 지목할 인덱스
result = [] # 제거되는 순서대로 담을 리스트

for i in range(N * K):
    pointer += K -1
    if pointer > len(arr) -1:
        while pointer > len(arr) -1:
            pointer -= len(arr)
    result.append(arr.pop(pointer))
    if not arr:
        break

new_result = ', '.join(map(str, result))
print(f'<{new_result}>')