import sys
input = sys.stdin.readline

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().strip().split())
'''
1. 원래 회전 초밥은 손님이 마음대로 초밥을 고르고, 
먹은 초밥만큼 식대를 계산하지만, 
벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 
1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공
만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공

가능한 한 다양한 종류의 초밥
'''
arr = []
for _ in range(n):
    x = int(input().strip())
    arr.append(x)

max_cnt = 0
left = 0
right = 0
while left != n:
    right = left + k
    case = set()
    coupon = True
    for i in range(left, right):
        i %= n
        case.add(arr[i])
        if arr[i] == c:
            coupon = False
    cnt = len(case)
    if coupon:
        cnt += 1
    max_cnt = max(cnt, max_cnt)
    left += 1
print(max_cnt)

