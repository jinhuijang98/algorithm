import sys
input = sys.stdin.readline

N = int(input())
ans = set()

for i in range(N + 1):
    for j in range(N + 1 - i):
        for k in range(N + 1 - i - j):
            l = N - i - j - k
            ans.add(i + 5 * j + 10 * k + 50 * l)
print(len(ans))