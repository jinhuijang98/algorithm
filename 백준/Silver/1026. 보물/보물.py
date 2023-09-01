import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))     # a에 있는 n개의 수가 순서대로
b = list(map(int, input().strip().split()))     # b에 있는 수가 순서대로



'''
모든 경우의 수 탐색
을 어케하노...

1, 1, 1, 6, 0으로 만들 수 있는 순열


'''


bb = b[:]

a.sort()
summ = 0

for i in range(n):
    x = max(bb)
    bb.remove(max(bb))
    summ += x * a[i]
print(summ)