T = int(input())

for tc in range(1, T+1):
    word = input()
    # x = word
    N=len(word)
    cnt = 0
    for i in range(len(word)//2):
        if word[i] != word[N-1-i]:
            cnt += 1

    if cnt==0:
        result =1
    else:
        result =0

    print(f'#{tc} {result}')