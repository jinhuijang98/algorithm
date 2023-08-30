import sys
input = sys.stdin.readline


# from collections import deque
# d = deque()

# n : 사진틀의 개수
n = int(input().strip())
# k : 총 추천 횟수
k = int(input().strip())

# arr : 추천 받은 순서
arr = list(map(int, input().strip().split()))

# 학생을 나타내는 번호 1 ~ 100
x = [0] * 101

a = []
for i in range(k):
    if len(a) < n and arr[i] not in a:
        a.append(arr[i])
        x[arr[i]] += 1
    elif arr[i] in a:
        x[arr[i]] += 1
    elif len(a) >= n:
        # 만약 길이가 n보다 크거나 같을 경우 for문을 돌면서
        # x 리스트 내의 arr[i] 값을 확인
        # 이 값들 중 가장 적은 학생 arr[j]의 값을 확인해서
        # 가장 작은 d.remove(arr[j])
        # x[arr[j]] = 0 으로 만들기
        min_v = 1000
        for j in range(n):
            if min_v > x[a[j]]:
                min_v = x[a[j]]
                min_i = a[j]
        a.remove(min_i)
        a.append(arr[i])
        x[arr[i]] += 1
        x[min_i] = 0
a.sort()
print(*a)
