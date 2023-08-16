import sys
input = sys.stdin.readline

# 피연산자의 개수
N = int(input())
# 후위 표기식
# fx = input()
fx = input().split('\n')[0]

# 갯수만큼 dict에 넣음
dict= {}
for i in range(N):
    dict[chr(i+65)] = int(input())


# 피연산자에 맞춰 후위 표기식에 값을 넣음
top = -1
stack = [0]*len(fx)
for i in range(len(fx)):
    if fx[i] not in '+-/*': # 숫자라면
        top +=1
        stack[top] = dict[fx[i]]
    else:
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if fx[i] == '*':
            top += 1
            stack[top] = op2 * op1
        elif fx[i] == '/':
            top += 1
            stack[top] = op1 / op2
        elif fx[i] == '+':
            top += 1
            stack[top] = op2 + op1
        else:
            top += 1
            stack[top] = op1 - op2

print(f'{stack[top]:.2f}')

