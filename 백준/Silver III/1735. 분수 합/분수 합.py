# 1735 분수 합

# 유클리드 호제법
'''
숫자 a, b 가 있을 때,
a를 b로 나눈 나머지와 b의 최대 공약수는 a와 b의 최대 공약수가 같다는 거을 의미


'''

# 최대공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 분자, 분모
a, b = map(int, input().strip().split())

c, d = map(int, input().strip().split())


qnswk = ((a*d) + (b*c))

qnsah = b*d


if qnswk > qnsah:
    x = gcd(qnswk, qnsah)
else:
    x = gcd(qnsah, qnswk)

hh = qnswk // x
gg = qnsah // x

print(hh, end=' ')
print(gg)