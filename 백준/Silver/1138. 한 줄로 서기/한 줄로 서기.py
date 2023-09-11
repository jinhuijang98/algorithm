import sys
input = sys.stdin.readline

# 사람의 수
n = int(input().strip())

# 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명 있는지 주어짐
arr = list(map(int, input().strip().split()))

'''
키가 1인 사람부터 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지
-> 줄을 선 순서대로 키 출력
'''
rlt = [n]
for i in range(n-2, -1, -1):
    # if arr[i] == 0:
    #     rlt.append(i+1)
    # else:
    rlt.insert(arr[i], i+1)
print(*rlt)