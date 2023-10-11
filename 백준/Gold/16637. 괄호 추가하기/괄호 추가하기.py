# 16637 괄호 추가하기


n = int(input().strip())

s = input()

result = (-2)**31
'''
1. 앞에 두 숫자가 먼저 계산될 때,
2. 앞에 말고 뒤에 두 숫자가 먼저 계산될 때,
'''
# 사칙연산하는 함수
def calcul(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2

# 재귀로 계속 계산해서 최댓값 갱신
def dfs(index, value):
    global result

    if index == n-1:
        result = max(result, value)
        return

    if index + 2 < n:
        # 앞에 두 숫자가 먼저 연산될 때
        dfs(index + 2, calcul(value, s[index + 1], int(s[index + 2])))

    if index + 4 < n:
        # 뒤 숫자가 먼저 계산될 때
        dfs(index + 4, calcul(value, s[index +1], calcul(int(s[index + 2]), s[index + 3], int(s[index + 4]))))

dfs(0, int(s[0]))
print(result)