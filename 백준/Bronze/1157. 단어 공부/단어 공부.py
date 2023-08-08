word = input()

# 글자를 모두 소문자로
new_word = word.upper()

# 갯수를 셀 딕셔너리 생성
cnt = {}
for cha in new_word:
    cnt[cha] = 0

# 갯수 세기
for cha in new_word:
    cnt[cha] += 1

# 최대 갯수 찾기
max_cnt = 0


for alpha in cnt:
    if max_cnt <= cnt[alpha]:
        max_cnt = cnt[alpha]

# 최댓값을 가진 알파벳 찾기
result = ''
max_num = 0
for alpha in cnt:
    if cnt[alpha] == max_cnt:
        result += alpha
        max_num += 1

if max_num > 1:
    print('?')
else:
    print(result)