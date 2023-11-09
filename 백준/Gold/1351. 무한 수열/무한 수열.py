# 1351 무한 수열
import sys
input = sys.stdin.readline


n, p, q = map(int, input().strip().split())

# 딕셔너리 선언
dict = {}
dict[0] = 1

def solution(n):

    # n번째 값이 저장되어있다면, 그대로 반환
    if (n in dict):
        return dict[n]
    # n번째 값이 저장되어있지 않다면, n번째 값을 계산 및 저장한 뒤, 반환
    else:
        dict[n] = solution(n//p) + solution(n//q)
        return dict[n]

print(solution(n))

