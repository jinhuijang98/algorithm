text = list(input())
'''
a와 b로만 이루어진 문자열이 주어질 때, a를 모두 연속으로 만들기 위해서 
필요한 교환의 회수를 최소로 하는 프로그램
원형이기 때문에 처음과 끝도 서로 인접
'''
# print(text)
cnt_a = 0

for i in text:
    if i == 'a':
        cnt_a += 1

# print(cnt_a)
cnt_b = len(text) - cnt_a
# print(cnt_b)

answer = ['a'] * cnt_a + ['b'] * cnt_b
# print(answer)

# 1. answer을 찾기
# 2. answer과 text와의 다른 것의 개수 // 2 => 정답
min_cnt = 99999
for i in range(len(answer)):
    cnt = 0
    for j in range(len(text)):
        if answer[j] != text[j]:
            cnt += 1
    if cnt//2 < min_cnt:
        min_cnt = cnt//2
    answer.append(answer.pop(0))
print(min_cnt)