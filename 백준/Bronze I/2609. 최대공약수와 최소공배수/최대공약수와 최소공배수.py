# 2609 최대 공약수와 최소 공배수

x, y = map(int, input().strip().split())

# 유클리드 호제법 사용

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)

x, y = max(x, y), min(x, y)

print(gcd(x, y))
print(int(lcm(x, y)))
