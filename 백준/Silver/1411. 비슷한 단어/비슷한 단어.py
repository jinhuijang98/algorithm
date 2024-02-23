# 1411 비슷한 단어
'''
알파벳 소문자로만 구성되어있다고 하였으므로, 이를 알파벳 대문자로 바꾸어 동일한 형태 찾기
'''
import sys
import math
input = sys.stdin.readline

replace_word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input().strip())

s_dict = {}

for _ in range(n):
    count = 0
    s = input().strip()

    for i in range(len(s)):
        # 만약 대문자로 변경된 문자라면 continue
        if s[i].isupper():
            continue
        # count에 해당하는 인덱스를 가진 알파벳 대문자로 변경
        s = s.replace(s[i], replace_word[count])
        count += 1

    if s not in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] += 1



# 똑같은 배열의 총 개수에서 2개씩 combination으로 뽑아서 동일할 경우 1쌍으로 취급
result = 0
for v in s_dict.values():
    result += math.comb(v, 2)
print(result)
