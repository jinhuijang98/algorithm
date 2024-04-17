import sys
input = sys.stdin.readline
##############################################
n, m = map(int, input().split())

ground = list(map(int, input().split()))

# 조교의 명령을 저장하는 리스트
order_answer = [0 for _ in range(n+1)]

# a-1 ~ b-1 까지 조교의 명령대로 수행
# b-1까지 k의 변화를 줘야 하므로 b에 저장해야 b-1에서 명령 수행
for _ in range(m):
    a, b, k = map(int, input().split())

    order_answer[a-1] += k
    order_answer[b] -= k

# 땅의 변화를 누적합으로 저장
change = 0

# 땅의 변화를 적용하여 땅의 높이 출력
for i in range(n):
    change += order_answer[i]
    print(ground[i] + change, end = " ")