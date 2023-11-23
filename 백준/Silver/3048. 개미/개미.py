import sys

n1, n2 = map(int, sys.stdin.readline().split())

ant1 = list(map(str,sys.stdin.readline().rstrip("\n")))
ant2 = list(map(str,sys.stdin.readline().rstrip("\n")))
t = int(sys.stdin.readline())

ant1.reverse() # 진행 방향을 바꾸기 위해
totalAnt = ant1 + ant2 # 두 개미 그룹의 위치

# t초동안 반복
for _ in range(t):
    # 반복문을 통해 두 개미 그룹을 확인
    for i in range(len(totalAnt) - 1):
        # 두 개미 그룹이 만났다면 위치를 바꾼다.
        if totalAnt[i] in ant1 and totalAnt[i + 1] in ant2:
            totalAnt[i], totalAnt[i + 1] = totalAnt[i + 1], totalAnt[i]

            # 위치를 바꾼 개미가 선두 개미이면 반복을 멈춘다.
            if totalAnt[i + 1] == ant1[-1]:
                break

print("".join(totalAnt))