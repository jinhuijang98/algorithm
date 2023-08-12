S = list(input())
# print(S)
# 비어있는 리스트 형성
arr = []
for i in range(len(S)):
    # S를 자른 값들을 arr에 옮기기
    arr.append(''.join(S[i:]))
# 정렬
arr.sort()
# 정렬한 순서대로 출력
for i in range(len(arr)):
    print(arr[i])