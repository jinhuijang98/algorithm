N = int(input())

arr = [i+1 for i in range(N)]
# print(arr)

new_list = []

while arr:
    x = arr.pop(0)
    try:
        arr.append(arr.pop(0))
    except:
        pass
    print(x, end= ' ')