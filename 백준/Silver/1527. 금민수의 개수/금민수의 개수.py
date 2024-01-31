# 1527 금민수의 개수
from itertools import product    
'''
4와 7로만 이루어진 수
a보다 크거나 같고, b보다 작거나 같은 자연수 중에 금민수인 것의 개수
'''
a, b = map(int, input().split())
x = len(str(a))
y = len(str(b))
'''
a ~ b까지 자리의 수를 확인
자릿수를 확인하고 자릿수가 그 사이이면서 4와 7로만 이루어진 모든 숫자를 만들고
그 숫자가 a와 b사이에 있다면 cnt += 1

중복 순열로 구현...
'''

cnt = 0

for i in range(x, y+1):
    lst = list(product([4, 7], repeat=i))
    for num in lst:
        n = int(''.join(map(str, num)))
        if a <= n <= b:
            cnt += 1
print(cnt)