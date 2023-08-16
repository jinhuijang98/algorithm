

T = 10
for tc in range(1, T+1):
    n = int(input())
    fx = input()
    susik = ''
    stack = [0]*n
    top = -1
    icp = {'*' : 2, '+' : 1}
    isp = {'*' : 2, '+' : 1}
    for x in fx:
        if x not in '+*':   # 피연산자라면
            susik += x
        else:
            if top == -1 or isp[stack[top]] <= icp[x]:  # 토큰의 우선순위가 더 높으면
                top += 1  # push
                stack[top] = x
            elif isp[stack[top]] > icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = x
    # stack 안에 연산자가 남아있는 경우가 있어서 이걸 다 빼줌!!
    # 마지막에 * 다음 +가 나오는경우
    for i in range(top+1):
        susik += stack[top]
        top -=1
    # print(susik)
    top = -1
    stack = [0]*n
    for x in susik:
        if x not in '+*':   # 피연산자라면
            top += 1        # push()
            stack[top] = int(x)
        else:
            op2 = stack[top]    # pop()
            top -= 1
            op1 = stack[top]    # pop()
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2
    print(f'#{tc} {stack[top]}')

