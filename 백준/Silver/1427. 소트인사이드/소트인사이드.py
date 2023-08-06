arr = list(map(int, input()))

new_list = []
for i in range(len(arr)):
    new_list.append(arr[i])


def bubble_sort(a, N):
    for i in range(N-1, -1, -1):
        for j in range(0, i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

x=bubble_sort(new_list, len(arr))
for i in range(len(new_list)):
    print(x[i], end="")