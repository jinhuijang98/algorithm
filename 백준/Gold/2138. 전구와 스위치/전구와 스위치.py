# 2138 전구와 스위치
import sys
input = sys.stdin.readline
'''
각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. 
i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 
즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 
1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, 
N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.
i = 0, ... , n-1
0번째 눌렀을 때, 
1번째 눌렀을 때
2번째 눌렀을 때...

n-1번째 눌렀을 때

---
1번 눌렀을 때 0/ x저장
2번 눌렀을 때 0/x 저장
3번....


'''
### 스위치를 눌렀을 때 상태 변경을 해주는 함수
def reverse(bulbs, count):
    for i in range(1, N-1):
        if bulbs[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulbs[j] = not bulbs[j]
    # 마지막 전구만 따로 처리
    if bulbs[N-1] != target[N-1]:
        count += 1
        bulbs[N-2] = not bulbs[N-2]
        bulbs[N-1] = not bulbs[N-1]
    if bulbs == target:
        return count
    else:
        return -1

N = int(input().strip())
off = list(map(bool, map(int, input().strip())))

# 0번째 스위치를 누른 상태를 저장하는 리스트
on = off.copy()
on[0] = not on[0]
on[1] = not on[1]

target = list(map(bool, map(int, input().strip())))

'''
i = 1일 때,
안 눌렀을 때 / 눌렀을 때 => 2
i = 2일 때,
i=1인거에 안눌렀을 때 / 눌렀을 때 => 

'''
if off==target:
    print(0)
else:
    # 0번째 전구를 안눌렀을 때
    count = reverse(off, 0)
    if count != -1:
        print(count)
    else:
        # 0번째 전구를 눌렀을 때
        count = reverse(on, 1)
        print(count if count else -1)

#
