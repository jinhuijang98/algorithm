def solution(a, b):
    if a == b:
        answer = a
    else:
        big = max(a, b)
        sma = min(a, b)
        answer = 0
        for i in range(sma, big+1):
            answer += i
    
    return answer