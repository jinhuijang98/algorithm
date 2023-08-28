import sys
input = sys.stdin.readline

# n : 스위치 개수
n = int(input().strip())

# 스위치의 상태 arr
arr = list(map(int, input().strip().split()))
# arr자체를 index로 사용하기 위해 0번째에 -1 값
arr.insert(0, -1)
# print(arr)
# 학생 수
stu = int(input().strip())

# 학생의 성별, 학생이 받은 수 stu_list
# stu_list[i][0] = 성별
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면 상태 바꿈
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
# 가장 많은 스위치를 포함하는 구간을 찾아서 그 구간에 속한 스위치의 상태를 모두 바꿈
# 구간에 속한 스위치 개수는 항상 홀수
stu_list = [[0]*2 for _ in range(stu)]
for i in range(stu):
    stu_list[i] = list(map(int, input().strip().split()))

for i in range(stu):
    # 남학생이라면
    if stu_list[i][0] == 1:
        # x는 남학생이 받은 수
        x = stu_list[i][1]
        i = 1
        xx = x
        while xx < len(arr):
            if arr[xx] == 0:
                arr[xx] = 1
            else:
                arr[xx] = 0
            i += 1
            xx = x * i
        # print(arr[1:])
    else:
        # y = 여학생이 받은 수
        y = stu_list[i][1]
        k = 1
        if arr[y] == 1:
            arr[y] = 0
        else:
            arr[y] = 1
        while y-k >= 0 and y+k < len(arr):
            if arr[y-k] == arr[y+k]:
                if arr[y-k] == 0:
                    arr[y-k] = 1
                    arr[y+k] = 1
                else:
                    arr[y-k] = arr[y+k] = 0
                k += 1
            else:
                break
        # print(arr[1:])

# 최종 출력
# 만약 20으로 나눈 몫이 1보다 크다면
new_arr = arr[1:]
while new_arr:
    if len(new_arr) <= 20:
        print(*new_arr)
        break
    else:
        for i in range(20):
            x = new_arr.pop(0)
            print(x, end=' ')
        print()