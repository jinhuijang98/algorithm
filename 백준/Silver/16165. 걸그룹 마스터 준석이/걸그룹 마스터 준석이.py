import sys
input = sys.stdin.readline

N, M = map(int, input().split())

girlgroups = {}

for _ in range(N):
    group_name = input().rstrip()
    girlgroups[group_name] = []
    members = int(input())
    for _ in range(members):
        girlgroups[group_name].append(input().rstrip())
    girlgroups[group_name].sort()
# print(girlgroups)

for _ in range(M):
    quiz = input().rstrip()
    quiz_type = int(input())
    if quiz_type == 0:
       for member in girlgroups[quiz]:
           print(member)
    else:
        for group in girlgroups:
            if quiz in girlgroups[group]:
                print(group)