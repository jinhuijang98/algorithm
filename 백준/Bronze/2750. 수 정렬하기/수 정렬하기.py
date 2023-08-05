N = int(input())

new_list = []
for i in range(N):
    arr = int(input())
    new_list.append(arr)
# print(new_list)

def sorting(a,N):
    for i in range(N-1, -1, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

sorting(new_list, N)
for i in range(N):
    print(new_list[i])
