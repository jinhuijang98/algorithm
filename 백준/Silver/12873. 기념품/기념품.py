# boj 캠프 참가자의 수

N = int(input())
arr = [i+1 for i in range(N)]
front = 0   # 초기값
x = 1
while len(arr) > 1:
    t = (front + (x**3) - 1) % len(arr)
      # 움직일 값
    arr.pop(t)            # 이전에 pop된 위치를 기억해야 함
    front = t           # 이전에 pop된 위치를 front에 기억
    # print(arr)
    x += 1
print(*arr)