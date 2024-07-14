# def solution(x):
#     answer = True
#     x = str(x)
#     a = 0
#     for i in range(len(x)):
#         a += int(x[i])
#     if int(x) % a != 0:
#         answer = False
#     return answer



def solution(n):
    total = 0
    for x in str(n):
        total += int(x)
    return n % total == 0