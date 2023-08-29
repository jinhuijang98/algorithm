X = int(input())

line = 1
while X > line: # X가 몇번째 줄인지 구함
    X -= line  
    line += 1

if line % 2 == 0:   # X가 짝수번째 줄이면 분자는 오름차순, 분모는 내림차순
    a = X
    b = line - X + 1
else:
    a = line - X + 1    # X가 홀수번째 줄이면 분자는 내림차순, 분모는 오름차순
    b = X

print(a, '/', b, sep='')