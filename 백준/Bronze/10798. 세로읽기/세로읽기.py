word = [list(map(str, input())) for _ in range(5)]
# 최대 열의 길이에 맞춰서 행렬 만들기
max_col = 0
# 열의 길이의 최댓값 구하기 -> count도 이용해서 해보기
for i in range(5):
    length = len(word[i])
    if max_col < length:
        max_col = length
# print(max_col)

# 최대 열의 길이에 맞춘 빈 리스트 만들기 (str로 만들면 편함)
fin_word = [['']*max_col for _ in range(5)]
# print(fin_word)

# fin_word의 각 자리에 word[i][j]넣기
# 여기서 주의해야 할 점은 열의 for문 돌릴 때 range범위를 len(word(i))로 넣어줘야 함!!!!
for i in range(5):
    for j in range(len(word[i])):
        fin_word[i][j] = word[i][j]
# print(fin_word)

# 이제 결과값 print => 열을 기준으로
for j in range(max_col):
    for i in range(5):
        print(fin_word[i][j], end="")