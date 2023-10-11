# 14888 연산자 끼워넣기
n = int(input())
A = list(map(int, input().split()))
p, mi, mul, di = map(int, input().split())

calcul = ['+']*p + ['-'] * mi + ['*'] * mul + ['//'] * di

min_val = 1000000000
max_val = -10000000000
'''
calcul로 수열을 만들어서
하나씩 집어 넣고 eval로 계산??
'''
path = [''] * (n-1)
visited = [False] * (n-1)
def calc(num1, cal, num2):
    if cal == '+':
        val = num1 + num2
    elif cal == '-':
        val = num1 - num2
    elif cal == '*':
        val = num1 * num2
    else:
        if num1 < 0:
            val = (-num1) // num2
            val = -val
        else:
            val = num1 // num2
    return val

def dfs(cnt):
    global min_val
    global max_val
    if cnt == n-1:
        path2 = path[:]
        # 연산 시작

        value = A[0]
        for j in range(n-1):
            value = calc(value,path[j],A[j+1])
        min_val = min(min_val, value)
        max_val = max(max_val, value)
        return

    for i in range(n-1):
        if not visited[i]:
            path[cnt] = calcul[i]
            visited[i] = True

            dfs(cnt+1)
            path[cnt] = ''
            visited[i] = False
dfs(0)
print(max_val)
print(min_val)