import sys
input = sys.stdin.readline

a, b = map(str, input().split())
a = int(a[::-1])
b = int(b[::-1])
print(int(str(a+b)[::-1]))



# 함수 이용
# a, b = map(str, input().split())
#
# def rev(x):
#     rev_x=''
#     for i in range(len(x)-1, -1, -1):
#         rev_x += x[i]
#     return int(rev_x)
#
# print(rev(str(rev(a) + rev(b))))