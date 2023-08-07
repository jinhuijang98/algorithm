T = int(input())

for tc in range(1, T+1):
    word = input()
    # x = word
    N=len(word)
    # 만약 문자열이 다른 게 있다면 1씩 증가시킬 변수
    cnt = 0
    # word 길이의 절반만큼 반복
    for i in range(len(word)//2):
        # 만약 다르다면 +1씩
        if word[i] != word[N-1-i]:
            cnt += 1
    # 모두 같다면 결과값은 1
    if cnt==0:
        result =1
    else:
        result =0

    print(f'#{tc} {result}')
