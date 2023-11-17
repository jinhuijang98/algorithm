# 20546 기적의 매매법
import sys
input = sys.stdin.readline


N = int(input().strip())

'''
준현이 => 살 수 있을만큼 다사기

'''

arr = list(map(int, input().strip().split()))

x_cash = N  # 보유 현금
x = 0       # x의 자산
x_stock_N = 0  # 보유 주식 수
# 주가 = arr[i]

for i in range(14):
    # 일단 주가를 확인 => 매수 가능 주식 수 = x_cash // arr[i]
    if x_cash // arr[i] > 0:
        x_stock_N += x_cash // arr[i]
        # 현금은 주가 * 매수 가능 주식 수 만큼 빼주기
        x_cash -= arr[i] * x_stock_N
    if x_cash == 0:
        break
    if x_cash < arr[i]:
        continue
x = x_cash + x_stock_N * arr[-1]

'''
성민이 
1. 모든 거래 전량 매수 & 전량 매도
    빚을 내서 주식을 하지는 않음
2. 3일 연속 가격이 전일 대비 상승하는 주식은 무조건 가격 하락
    현재 소유한 주식의 가격이 3일째 상승하면 전량 매도(판다)
    전일과 오늘의 주가가 동일하다면 가격 상승 x
3. 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승
    => 전량 매수(산다)
    전일 = 오늘 => 가격 하락 x

'''
y_cash = N  # 보유 현금
y = 0       # 보유 자산
y_stock_N = 0   # 보유 주식 수
# 주가 = arr[i]
flag = arr[0]
# 상승 => 판다
up = 0
# 하락 => 산다
down = 0
for i in range(1, 14):
    if flag < arr[i]:
        up += 1
        down = 0
        flag = arr[i]
    elif flag > arr[i]:
        down += 1
        up = 0
        flag = arr[i]
    elif flag == arr[i]:
        up = 0
        down = 0
        flag = arr[i]
    if up >= 3 or down >= 3:
        if up >= 3:
            y_cash += arr[i] * y_stock_N
            y_stock_N = 0
            up = 0
        elif down >= 3:
            if y_cash >= arr[i]:
                y_stock_N += y_cash // arr[i]

                y_cash -= arr[i] * (y_cash // arr[i])

y = y_cash + y_stock_N * arr[-1]

if x > y:
    print("BNP")
elif x == y:
    print("SAMESAME")
else:
    print("TIMING")