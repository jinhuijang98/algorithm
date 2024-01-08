# 10427 빚쟁이

'''
최근 N번 돈을 빌렸고, 그때마다 빌린돈이 a(1), a(2), ... , a(n)
민균이에게 m번의 빚을 갚으라고 명령하면 민균이는 n번 중 아무렇게나 m번을 고르고,
고른 것 중에서 가장 많은 돈을 빌렸을 때 빌린 돈 x m을 갚아야 함
이렇게 하면 민균이가 김우현 연구소에 갚아야 하는 돈은 (빌린 돈 + 추가적으로 더 갚아야 할 돈)
어떻게든 추가적으로 더 갚아야 할 돈을 최소한으로 하기
s(m)을 김우현 연구소가 민균이에게 m번의 빚을 갚으라고 명령했을 때 민균이가 m번을 선택하여
추가적으로 더 갚아야 할 돈을 최소한으로 하고 싶어 함
S(m)을 김우현 연구소가 민균이에게 m번의 빚을 갚으라고 명령했을 때 민균이가 m번을 선택하여 추가적으로
갚아야 하는 돈의 최솟값


차이가 최소가 되게 선택하면 됨
'''


import sys
input = sys.stdin.readline

# def Sort(list_):
#     for i in range(len(list_)):
#         for j in range(len(list_) - i - 1):
#             if list_[j] > list_[j+1]:
#                 list_[j], list_[j+1] = list_[j+1], list_[j]


t = int(input())

for _ in range(t):
    n, *money = map(int, input().split())

    # 각 비용의 차이를 최소화 하기 위한 정렬
    money.sort()
    # print(money)

    answer = 0

    # S(1) ~ S(N)까지 구하기 위한 반복
    # S(1) ==  0 이므로 2부터 반복
    for i in range(2, n+1):
        sum_ = 0
        # 첫 0~i 까지 구간합
        for j in range(i):
            sum_ += money[j]
        min_value = money[i-1]*i - sum_

        # j~j+i 까지 구간합을 구해서 빚의 차이 계산후 최소값 갱신
        for j in range(i, n):
            sum_ = sum_ + money[j] - money[j-i]
            min_value = min_value if min_value < (money[j] * i) - sum_ else (money[j] * i) - sum_

        # S(i)의 최소값 더하기
        answer += min_value

    print(answer)
# for _ in range(T):
#     n, *arr = map(int, input().strip().split())
#     arr.sort()
#     rlt = 0
#     rlt_sum = 100000000000000000000000
#     x = 1
#     while x < n:
#         cnt = 0
#         for i in range(n):
#             max_sum = arr[i] * x
#         for j in range()
#
#
#                 cnt += arr[i] - arr[j]
#                 # print(cnt)
#                 rlt_sum = min(cnt, rlt_sum)
#         rlt += rlt_sum
#         x += 1
#     print(rlt)