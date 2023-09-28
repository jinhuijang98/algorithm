'''
동석차 없이 등수 매기기
예상 등수를 바탕으로 임의로 등수
N명의 사람들의 불마도의 총 합을 최소로 하면서
학생들의 등수 매기기
불만도의 합을 최소로 할 때 그 불만도 출력
'''

import sys
input = sys.stdin.readline

n = int(input().strip())
# 예상 등수
arr = []
for _ in range(n):
    x = int(input().strip())
    arr.append(x)

# 석차
grade = [i+1 for i in range(n)]

# 예상 등수와 석차의 차이를 최소로 하는 프로그램 => 최대한 예상 등수와 동일하게
arr.sort()

# grade와 arr이 동일한건 제거
# for i in arr:
#     if i in grade:
#         arr.remove(i)
#         grade.remove(i)

x = len(arr)
k = 0
total = 0
while k < x:
    total += abs(arr[k] - grade[k])
    k += 1
print(total)