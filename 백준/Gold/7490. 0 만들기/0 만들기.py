import itertools


t = int(input())

# def cal(x, y):


result = []
operator = [' ', '+', '-']

def recursion(now, ans):
    # 현재 수가 N일 경우 더이상 연산자를 붙이지 않고 결과를 계산하여 식을 빠져나옴
    # 이제 연산을 해야하는 숫자가 n+1이라는 것은 n까지의 연산이 끝났다는 의미이므로!
    if now == n+1:
        calc(ans)
        return
    # 아닌 경우 현재 수에 +1하고 모든 연산자를 붙여 함수를 재호출
    for o in operator:
        recursion(now+1, ans+o+str(now))

def calc(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        result.append(ans)



for _ in range(t):
    n = int(input())
    # recursion(now, ans)
    # 1부터 수를 증가시키면서 재귀적으로 함수를 호출시키며 모든 식을 구하고 결과값을 계산
    # ans는 연산을 1부터 시작한다는 의미!?
    # 앞의 2는 now... => 이제 연산을 해야하는 숫자
    recursion(2, '1') # n은 3부터
    result.append(' ')
    # arr = [i+1 for i in range(n)]
    '''
    백트래킹 어떻게 하더라..
    '''
    # 연산의 갯수는 n-1개 / +, -, ' '
    # 연산의 경우의 수를 만들기
    # plus = ['+'] * (n-1)
    # minus = ['-'] * (n-1)
    # sum_ = [' '] * (n-1)
    # npr = itertools.permutations()

print(*result, sep='\n')