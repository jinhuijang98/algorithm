# 15889 호 안에 수류탄이야!!

import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())

arr1 = list(map(int, input().strip().split()))

'''

'''


if n > 1:
    arr2 = list(map(int, input().strip().split()))
    i = 0
    check = True
    while i < n-1 and check is True:
        x = arr1[i]
        nx = arr1[i] + arr2[i]
        # max_v = arr1[i] + arr2[i]
        for k in range(0, n-1):
            if arr1[k] + arr2[k] >= nx and arr1[k] <= nx:
                nx = max(arr1[k] + arr2[k], nx)
                i = k
                if arr1[k] + arr2[k] >= arr1[-1]:
                    check = False
                    print('권병장님, 중대장님이 찾으십니다')
                    exit()
        else:
            check = False
            print('엄마 나 전역 늦어질 것 같아')
            break
    else:
        print('엄마 나 전역 늦어질 것 같아')


else:
    print('권병장님, 중대장님이 찾으십니다')



