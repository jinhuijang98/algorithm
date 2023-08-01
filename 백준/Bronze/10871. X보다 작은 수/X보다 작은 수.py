N, X = map(int, input().split())
A = list(map(int,input().split()))
new_list = []
for x in A:
    if x < X:
        new_list.append(x)
    # for nl in new_list:
for nl in new_list:
    print(nl, sep=" ")