# 17281 야구?
import sys
from itertools import permutations
input = sys.stdin.readline
# n : 이닝 수
n = int(input().strip())


# 아인타팀이 얻을 수 있는 최대 점수 출력하기
# 각 선수가 이닝에서 얻는 결과가 1번 이닝부터 N번 이닝까지 순서대로 주어짐

# 경기 중에는 타순을 변경할 수 없으며, 9번 타자가 공을 쳤는데 3아웃이 발생하지 않은 상태면
# 이닝은 끝나지 않고 1번 타자가 다시 타석에 섬. 타순은 이닝이 변경되어도 순서를 유지해야 함
# 예를 들어, 2이닝에 6번 타자가 마지막 타자였다면, 3이닝은 7번 타자부터 타석에 섬
'''
아인타 팀의 선수는 총 9명이 있고, 1번부터 9번까지 번호가 매겨져 있다. 
아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정했다. 
이제 다른 선수의 타순을 모두 결정해야 한다. 
=> 이게 무슨 소린가 했더니 4번타자는 정해져있다는 말이었구나...
4번 타자는 정해져있고(1번 선수), 나머지 8명의 타자에게 타순을 부여하는 문제
8! -> 4만개 
아인타는 각 선수가 각 이닝에서 어떤 결과를 얻는지 미리 알고 있다. 
가장 많은 득점을 하는 타순을 찾고, 그 때의 득점을 구해보자.

각 이닝에는 아웃을 기록하는 타자가 적어도 한 명 존재한다.
각 행마다 모든 경우의 수를 세면서 확인..........해야 하는데


경우의 수는 0, 1, 2, 3, 4
0의 개수, 1의 개수, 2의 개수, 3의 개수, 4의 개수를 세
그리고 모든 경우의 수를 확인해 => 이렇게 하기에는 뒤의 이닝에 있어서
경우의 수가 모두 달라짐..
그럼 그냥 냅다 돌리면 되나?
모든 경우의 수를?
가장 높은 점수 기록?
'''

inning = [list(map(int, input().strip().split())) for _ in range(n)]
# print(arr)

max_score = 0

def game(line_ups):
    # 라인업의 index를 가져오는 hitter_idx 0~8
    hitter_idx = 0
    score = 0
    for each_inning in inning:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            # each_inning[line_ups[hitter_idx]]의 의미는 ? 각 이닝의 몇번째 값을 가져올건데? 이걸 line_ups에서 순열로 뽑아놨으니까
            if each_inning[line_ups[hitter_idx]] == 0:
                out += 1
            elif each_inning[line_ups[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif each_inning[line_ups[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif each_inning[line_ups[hitter_idx]] == 3:
                score += (b2 + b3 + b1)
                b1, b2, b3 = 0, 0, 1
            elif each_inning[line_ups[hitter_idx]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0

            hitter_idx = (hitter_idx + 1) % 9

    return score

for line_ups in permutations(range(1, 9), 8):
    line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
    max_score = max(max_score, game(line_ups))

print(max_score)