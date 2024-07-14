def solution(s):
    s = s.split()
    s = list(map(int, s))
    s.sort()
    answer = ''
    answer += str(s[0])
    answer += ' '
    answer += str(s[-1])
    return answer