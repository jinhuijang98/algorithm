import sys
input = sys.stdin.readline

rlt = 0
arr = []
for i in range(9):
    height = int(input())
    arr.append(height)
    rlt += height
x = rlt - 100   # 난쟁이가 아닌 두 수의 합
arr.sort()
# new_list = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == x:
            x1 = arr[j]
            x2 = arr[i]
            break
arr.remove(x1)
arr.remove(x2)
for i in range(len(arr)):
    print(arr[i])
