for tc in range(1, 11):
    N = int(input())
    fx = input()
    # print(len(fx))
    susik = ''
    stack = [0] * N
    top = -1
    for x in fx:
        if x not in '+':  # 피연산자
            susik += x
        else:  # + 라면
            top += 1  # push
            stack[top] = x
    while top > -1:
        susik += stack[top]
        top -= 1 # stack에서 top을 pop해서 susik에 넣어준다(연산자들)
    # stack = [0]*N'
    # print(susik)
    top = -1
    # susik = '6528-*2/+'
    for x in susik:
        if x not in '+-/*':  # 피연산자면...
            top += 1  # push()
            stack[top] = int(x)
        else:
            op2 = stack[top]  # pop()
            top -= 1
            op1 = stack[top]  # pop()
            top -= 1
            if x == '+':  # op1 + op2
                top += 1
                stack[top] = op1 + op2

    print(f'#{tc} {stack[top]}')
