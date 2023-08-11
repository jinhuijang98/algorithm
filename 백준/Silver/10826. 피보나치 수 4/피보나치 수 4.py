n = int(input())
arr = [0, 1]
for i in range(len(arr), n+1):
    arr.append(arr[-1]+arr[-2])
print(arr[n])