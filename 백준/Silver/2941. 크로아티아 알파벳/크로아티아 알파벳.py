x = str(input())
d = ["c=", "c-", "dz=", "d-", "lj", "s=", "z=", "nj"]

for s in d:
    x = x.replace(s, "1")

print(len(x))