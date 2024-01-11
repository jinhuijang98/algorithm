# 9466 텀 프로젝트
import sys
# from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방
'''
'문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 함.
프로젝트 팀원 수에는 제한 x
모든 학생들은 프로젝트를 함께하고 싶은 학생 선택해야 함. (단, 단 한 명만 선택할 수 있음)
혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능.
학생들이 s1, s2, ..., sr
s1이 s1을 선택하는 경우, s1이 s2를 선택하고, s2가 s3를 선택하고, ..., sr-1이 sr을 선택하고,
sr이 s1을 선택하는 경우에만 한 팀이 될 수 있음.
그니까 연결이 되어야 한다는 거잖아... dfs로 연결이 되지 않은 사람의 수?? 그냥 끝나버리면
cnt += 1
부모랑 자식 관계? 
자기 자신을 선택하면 팀에 속함!!

'''

def dfs(x):
    global result
    visited[x] = True
    # cycle을 이루는 팀을 확인하기 위함
    cycle.append(x)
    next_stu = graph[x]

    # 방문 했고, 사이클이 가능하다면?
    if visited[next_stu]:
        if next_stu in cycle:
            # 사이클이 되는 구간부터만 팀을 이룸
            # next_stu가 cycle에 있다는 거니까 next_stu의 인덱스부터 슬라이싱해서 result에 더해줌
            result += cycle[cycle.index(next_stu):]
        return
    else:
        dfs(next_stu)
    #



T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    # stu = [i+1 for i in range(n)]
    graph = [0] + list(map(int, input().strip().split()))
    # 방문 여부
    visited = [True] + [False] *(n)
    result = []
    # 사이클을 발견하면 담을 set

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    # 팀을 결성하지 못한 멤버
    print(n - len(result))


