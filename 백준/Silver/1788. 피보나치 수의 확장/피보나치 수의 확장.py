# 1788 피보나치 수의 확장
# 다시 
# n이 양수일때 음수일때 나누기보다는 이런식으로 append해서 구할 수 있구나
n = int(input())

s = [0, 1]

for i in range(2, abs(n)+1):
    s.append((s[i-1] + s[i-2]) % 1000000000)
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(s[abs(n)])

