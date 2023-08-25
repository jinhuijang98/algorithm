import sys

input = sys.stdin.readline

# n : 학생의 수
n = int(input().strip())
# 줄을 선 차례대로 학생들이 뽑은 번호
arr = list(map(int, input().strip().split()))

# 학생의 수만큼 list만들기
stu = [i+1 for i in range(n)]

# 줄 선 학생 list
#
line_stu = []


# stu[0] => arr[0]
for i in range(n):
    line_stu.insert(len(line_stu) - arr[i], stu[i])
print(*line_stu)