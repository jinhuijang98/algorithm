T = int(input())

for tc in range(T):
    arr = list(map(str, input().split()))
    # print(arr)
    # 뒤집어진 문자열을 넣을 리스트
    new_list = []
    for i in range(len(arr)):
        # 거꾸로 만들 문자열을 ''을 이용해 형성
        reverse_word = ''
        # print(arr[i])
        # 각 단어의 길이가 2 이상이라면
        if len(arr[i]) >= 2:
            # 단어 뒤집어서 새로운 리스트에 넣기
            for j in range(len(arr[i])):
                reverse_word = arr[i][j] + reverse_word
            new_list.append(reverse_word)
        # 그렇지 않다면
        else:
            # 원래 문자 그대로 new_list에 넣기
            new_list.append(arr[i])
    # 출력 방식은 new_list의 원소 하나하나를 띄어쓰기로 구분해 print
    for i in range(len(new_list)):
        print(new_list[i], end=" ")