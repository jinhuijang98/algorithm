import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
start, end = 0, 0
size, size_max = 0, 0
flag = 1

for start in range(n):
    while cnt <= k and flag:
        if lst[end] % 2:  # 현재 수가 홀수라면
            if cnt == k:
                break
            cnt += 1
        size += 1
        if end == n - 1:  # 끝 포인터가 리스트의 마지막 원소에 도달했다면
            flag = 0
            break
        end += 1

    # 가장 긴 짝수 부분수열의 길이와 현재 짝수 부분수열의 길이를 비교해서 업데이트
    if size_max < size - cnt:
        size_max = size - cnt

    # start를 한 칸 뒤로 이동시켜주기 위한 준비
    if lst[start] % 2:
        cnt -= 1
    size -= 1
print(size_max)