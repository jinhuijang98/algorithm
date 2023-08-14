import sys
S = sys.stdin.readline().strip() + ' '
stack = []
result = ''  # 결과물 출력
cnt = 0  # 괄호 안에 있는지 여부
for i in S:
    if i == '<':
        cnt = 1
        for _ in range(len(stack)):  # 괄호 만나기 이전 stack 애들 비워주고 다 뒤집어서 더gka
            result += stack.pop()
    stack.append(i)

    if i == '>':
        cnt = 0
        for _ in range(len(stack)):  # 괄호 안에 있는 애들은 뒤집지 말고 더gkrl
            result += stack.pop(0)

    if i == ' ' and cnt == 0:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '  # 마지막에 공백 살려주기
print(result)