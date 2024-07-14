def solution(x, n):
    answer = []
    a = x
    i = 0
    while i < n:
        answer.append(a)
        a = a+x
        i += 1
    return answer
