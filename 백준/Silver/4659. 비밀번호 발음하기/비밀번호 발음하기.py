'''
모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
'''
import sys
input = sys.stdin.readline
arr = []
while True:
    x = input().strip()
    if x != "end":
        arr.append(x)
    else:
        break
# 1. 모음(a,e,i,o,u) 하나를 반드시 포함
vowel = ['a', 'e', 'i', 'o', 'u']
check1 = [False] * len(arr)
for j in range(len(arr)):
    for i in vowel:
        if i in arr[j]:
            check1[j] = True
            break
# for i in range(len(check1)):
#     if check1[i] is False:
#         print(f'<{arr[i]}> is not acceptable.')
#         arr.remove(arr[i])


# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
for i in range(len(arr)):
    if check1[i] is True and len(arr[i])>=3:
        vow = 0
        con = 0
        for j in range(len(arr[i])):
            # vow = [0] * len(arr[i])
            if arr[i][j] in vowel:
                vow += 1
                if vow >= 3:
                    check1[i] = False
                    break
                con = 0
            else:
                con += 1
                if con >= 3:
                    check1[i] = False
                    break
                vow = 0

# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
for i in range(len(arr)):
    if check1[i] is True:
        for k in range(1, len(arr[i])):
            if arr[i][k] == arr[i][k-1]:
                if arr[i][k-1:k+1] == 'ee' or arr[i][k-1:k+1] == 'oo':
                    continue
                else:
                    check1[i] = False
                    break
# print(check1)
# 출력
for i in range(len(check1)):
    if check1[i] is True:
        print(f'<{arr[i]}> is acceptable.')
    else:
        print(f'<{arr[i]}> is not acceptable.')