import sys
input = sys.stdin.readline

'''
1 1 7
1 2 6
1 3 5
1 4 4
2 2 5
2 3 4
3 3 3

[0] * 3
a[0] + a[1] + a[2] = n
and a.sort()
a[2] < a[0] + a[1]
cnt += 1

a[0] <= a[1] <= a[2] 
'''
n = int(input().strip())

# 더해서 n이 되는 자연수의 조합 모두 구하기
# def solution(n):
#     number = [n-n//2-1, 1]
#     global answer
#     answer = []
#     while True:
#         if len(number) == 2:
#             answer.append(number.copy())
#         temp = number.pop()
#         if temp != 1:
#             number.append(temp - 1)
#             number.append(1)
#         else:
#             sum = 2
#             for _ in range(len(number)):
#                 if number and number[-1] == 1:
#                     sum += 1
#                     number.pop()
#             if not number:
#                 break
#             pivot = number.pop() - 1
#             number.append(pivot)
#             while sum > pivot:
#                 number.append(pivot)
#                 sum -= pivot
#             number.append(sum)
#     return answer
# if n <= 2:
#     print(0)
# else:
#     solution(n)
#     print(len(answer))
    # print(answer)
    # cnt = 0
    # for i in range(len(answer)):
    #     if answer[i][0] < answer[i][1] + answer[i][2]:
    #         cnt += 1
    # print(cnt)
cnt = 0
check = False
for i in range(1, n//3+1):
    for j in range(i, (n-i)//2+1):
        k = n - i - j
        if k < i + j:
            cnt += 1
print(cnt)