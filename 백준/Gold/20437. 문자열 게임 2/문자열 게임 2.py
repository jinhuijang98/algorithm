import sys
input = sys.stdin.readline
'''
인덱스 부분만 처리할 수 있었으면 바로 풀 수 있었을텐데,,,

'''
t = int(input())

for _ in range(t):
    w = input().strip()
    k = int(input())

    # 각 문자의 개수를 세는 딕셔너리
    count_char_dict = {}

    # 각 문자의 개수 세기
    for char in w:
        count_char_dict[char] = count_char_dict.get(char, 0) + 1

    # 결과와 관련된 변수
    check = False
    max_answer = -1
    min_answer = len(w)

    # 특정 문자열의 위치 index를 저장하는 딕셔너리
    check_dict = {}

    # 모든 문자열에 대해서
    for i in range(len(w)):
        # 해당 문자열이 k개 이하이면 다음 문자
        if count_char_dict[w[i]] < k:
            continue

        # k개 이상인 문자를 찾으면 정답이 있음
        check = True
        # 해당 문자열을 key로하고 index리스트를 value로 갖는 딕셔너리
        check_dict[w[i]] = check_dict.get(w[i], []) + [i]

    # 딕셔너리를 돌면서
    for key, value_list in check_dict.items():
        # 인덱스 번호를 바탕으로
        for i in range(len(value_list) - k + 1):
            # 최대 최소 갱신
            max_answer = max(max_answer, value_list[i+k-1] - value_list[i] +1)
            min_answer = min(min_answer, value_list[i + k - 1] - value_list[i] + 1)

    # 정답이 있으면 출력
    if check:
        print(min_answer, max_answer)

    # 없으면 -1출력
    else:
        print(-1)