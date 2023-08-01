new_list = []
# 새로운 리스트 안에 1~30까지 변수 넣기
for i in range(1,31):
    new_list.append(i)

# 길이가 2가 되면 멈춤 3까지 반복.
while len(new_list) > 2:
    n = int(input())
    # 새로운 리스트안에 있는 n을 제거
    new_list.remove(n)
    
# 정렬 후 print
new_list.sort()
for i in new_list:
    print(i)