T = int(input())
for tc in range(1, T+1):
    # 우선 뒤집힌 문자열 딕셔너리로 만들어 놓기
    dict = {'b' :'d',
            'd' :'b',
            'p' : 'q',
            'q' : 'p'}
    # 뒤에서부터 출력
    text = list(input())
    new_word = ['']*len(text)
    # print(text)
    for i in range(len(text)-1, -1, -1):
        new_word.append(dict[text[i]])
    x=''.join(new_word)
    print(f'#{tc} {x}')