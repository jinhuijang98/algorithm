card = [input().split() for _ in range(5)]

# color = []
num = []
for i in range(5):
    # color.append(card[i][0])
    num.append(int(card[i][1]))

color_cnt = [0] * 4
for i in range(5):
    if card[i][0] == 'R':
        color_cnt[0] += 1
    elif card[i][0] == 'B':
        color_cnt[1] += 1
    elif card[i][0] == 'Y':
        color_cnt[2] += 1
    elif card[i][0] == 'G':
        color_cnt[3] += 1
# print(color_cnt)

num_cnt = [0] * 10
for i in range(5):
    num_cnt[int(card[i][1])] += 1
# print(num_cnt)

# 7번 조건 확인용
seven = 0
seven_lst = []
for i in range(10):
    if num_cnt[i] == 2:
        seven_lst.append(i)
        seven += 1
# check1으로 몇장의 카드가 색깔이 같은지 파악
check1 = max(color_cnt)
# check2로 몇장의 카드가 숫자가 같은지 파악
check2 = max(num_cnt)
# check3로 숫자가 연속됐는지 파악 (max_cnt)
max_cnt = 0
cnt = 0
for i in range(1, 10):
    if num_cnt[i] >= 1:
        cnt += 1
    if num_cnt[i] == 0:
        if max_cnt < cnt:
            max_cnt = cnt
            cnt = 0
if max_cnt < cnt:
    max_cnt = cnt
# print(max_cnt)

# 1. 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때
if check1 == 5 and max_cnt == 5:
    # 점수는 가장 높은 숫자에 900을 더한다
    print(max(num) + 900)
# 2. 카드 4장의 숫자가 같은 경우
elif check2 == 4:
    #  점수는 같은 숫자에 800을 더한다
    print(num_cnt.index(max(num_cnt)) + 800)
# 3. 카드 3장의 숫자가 같고, 나머지 2장도 숫자가 같을 때
elif 2 in num_cnt and 3 in num_cnt:
    # 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다
    print(num_cnt.index(3) * 10 + num_cnt.index(2) + 700)
# 4. 5장의 카드 색깔이 모두 같을 때
elif check1 == 5:
    # 가장 높은 숫자에 600을 더한다
    print(max(num) + 600)
# 5. 카드 5장의 숫자가 연속적일 때
elif max_cnt == 5:
    # 가장 높은 숫자에 500을 더한다.
    print(max(num) + 500)
# 6. 카드 5장 중 3장의 숫자가 같을 때
elif check2 == 3:
    # 같은 숫자에 400을 더한다.
    print(num_cnt.index(3) + 400)
# 7. 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때
elif seven == 2:
    # 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
    print(seven_lst[1] * 10 + seven_lst[0] + 300)
# 8. 카드 5장 중 2장의 숫자가 같을 때
elif seven == 1:
    # 같은 숫자에 200을 더한다.
    print(num_cnt.index(check2) + 200)
else:
    print(max(num) + 100)
