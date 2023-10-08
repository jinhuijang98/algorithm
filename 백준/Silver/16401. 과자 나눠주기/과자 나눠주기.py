# 과자 나눠주기
import sys
input = sys.stdin.readline

'''
조카들에게 최대한 긴 과자 나눠주기
나눠준 과자의 길이가 모두 동일하게
M명의 조카, N개의 과자가 있을때
줄 수 있는 막대 과자의 최대 길이
막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만,
과자를 하나로 합칠 수는 x
모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면 0 출력
'''

M, N = map(int, input().strip().split())

L = list(map(int, input().strip().split()))
'''
7 7 (6) 7 7 (6) 7 7 7 
'''
start = 1
end = max(L)
result = 0
while start <= end:
    mid = (start + end) //2
    # cnt : mid와 같아질 수 있는 것의 개수
    cnt = 0
    # 만약 나눌 수 없다면 0출력

    for i in L:
        if i >= mid:
            cnt += (i//mid)
    if cnt >= M:
        result = max(result, mid)
        start = mid + 1

    else:
        end = mid - 1

print(result)
