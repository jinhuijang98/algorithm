import sys
input = sys.stdin.readline

# n : 온도를 측정한 전체 날짜의 수
# k : 합을 구하기 위한 연속적인 날짜의 수
n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# 최종 온도의 합이 최대가 되는 값
result = 0
# # 처음 k개의 합을 먼저 구한 후에 제일 앞의 값 빼고 뒤의 값 더하는 방식으로 시간초과 해결하기
# for i in range(n-k+1):
#     # 매번 시행할 때마다 찾는 k개의 합
#     rlt = 0
#     for j in range(k):
#         rlt += arr[i+j]
#     if result < rlt:
#         result = rlt
rlt = 0
for i in range(k):
    rlt += arr[i]
# rlt : 초기 값
result = rlt
for i in range(n-k):
    rlt -= arr[i]
    rlt += arr[i+k]
    if result < rlt:
        result = rlt
print(result)