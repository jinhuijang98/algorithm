N = str(input())

new_num = 0
num_list = []

# 3의 특징과 10의 특징을 모두 가져야 함
for i in range(len(N)):
    num_list.append(N[i])
    new_num += int(N[i])

for i in range(len(N)):
    cnt = 0
    # 확인할 값으로
    if int(N[i]) == 0:
        break
    else:
        cnt += 1
# print(cnt)

# for i in range(len(N)):



# 만약 cnt가 0이라면 10으로 나누어 떨어짐

if cnt == 0 and new_num % 3 == 0:
    num_list.sort(reverse=True)
    # print(num_list)
    print(''.join(num_list))

else:
    print(-1)