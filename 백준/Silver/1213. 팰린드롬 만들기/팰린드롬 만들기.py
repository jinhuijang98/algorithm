text = input()
'''
길이 수만큼의 0으로 만든 배열을 만들고 
text의 길이가 짝수라면 모든 글자가 짝수개여야 팰린드롬 가능
text의 길이가 홀수라면 하나의 글자를 제외하고는 모든 글자가 짝수개여야 팰린드롬 가능

'''
text_cnt = [0 for _ in range(26)]
for te in text:
    text_cnt[ord(te)-65] += 1

odd = 0
odd_alpha = ''
alpha = ''
for i in range(26):
    if text_cnt[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i+65)
    alpha += chr(i+65) * (text_cnt[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha + odd_alpha + alpha[::-1])

# x = len(text)
# dic = {}
# for i in range(len(text)):
#     dic.setdefault(text[i], 0)
#     dic[text[i]] += 1
# print(dic)
#
# # 홀수의 개수 count
# cnt = [0]
# x = list(dic.values())
#
# for i in range(len(x)):
#     if x[i] % 2:
#         cnt[0] += 1
#
# # 텍스트의 개수가 2로 나누어떨어지면서 홀수의 개수가 없다면 => 펠린드롬 가능
# if (len(text) % 2 == 0 and cnt[0] == 0) or (len(text) % 2 == 1 and cnt[0] == 1):
#     # if len(text) % 2 == 0 and cnt[0] == 0:
#     # if len(text) % 2 == 0:
#     x1 = len(text)//2
#     text1 = text[::2]
#     text1.sort
#     print(text1)
#     text2 = text[1::2]
#     text2.sort(reverse=True)
#     print(text2)
#         # for i in range(len(text)):
#         #     text[]
#
# else:
#     print("I'm Sorry Hansoo")
# # 텍스트의 개수가 홀수이면서 홀수의 개수가 1개라면 => 펠린드롬 가능
#
# # 이 외에는 쏘리