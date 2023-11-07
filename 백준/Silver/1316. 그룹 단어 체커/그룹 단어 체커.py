import sys
input = sys.stdin.readline


n = int(input().strip())
arr = [input().strip() for _ in range(n)]
# print(arr)
cnt = 0
for i in range(n):
    dic = {}
    for j in range(len(arr[i])):
        dic[arr[i][j]] = dic.setdefault(arr[i][j], 0) + 1
    # 딕셔너리 키값을 value만큼 반복해서 새로운 리스트 만들기
    new_str = ''
    for k in dic:
        new_str += (k*dic[k])
    if arr[i] == new_str:
        cnt += 1
print(cnt)