


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    dic = {'0001101': 0, '0011001': 1,
           '0010011': 2, '0111101': 3,
           '0100011': 4, '0110001': 5,
           '0101111': 6, '0111011': 7,
           '0110111': 8, '0001011': 9}
    check = True
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] != '0':
                start_row = i
                final_col = j
                check = False
                break
        if check is False:
            break
    result = arr[start_row][final_col-55:final_col+1]
    # 8개씩 잘라서 확인
    i = 0
    fin_result1 = ''
    fin_result2 = ''
    while i < 56:
        rlt = result[i:i+7]
        if (i+7)%2:
            fin_result1 += str(dic[rlt])
        else:
            fin_result2 += str(dic[rlt])
        i += 7
    # 홀수 자리의 합
    odd = 0
    for j in fin_result1:
        odd += int(j)
    even = 0
    for k in fin_result2:
        even += int(k)
    if (odd*3+even) % 10 == 0:
        print(f'#{tc} {odd+even}')
    else:
        print(f'#{tc} 0')