import sys
input = sys.stdin.readline

# n : 후보의 수
n = int(input())
arr = list(int(input().strip()) for _ in range(n))
# x : 다솜이를 찍는 사람의 수
x = arr[0]
'''



'''
cnt = 0
# 후보자가 한명인 경우 0 출력
if len(arr) == 1:
    print(0)
else:
    # 그렇지 않다면 다솜이 제외한 후보를 찍는 사람의 수를 가져와서 정렬하고 max 값과 비교해나감
    new_list = arr[1:]
    # new_list.sort()
    while x <= max(new_list):
        new_list.sort()
        new_list[-1] -= 1
        x += 1
        cnt += 1

    print(cnt)