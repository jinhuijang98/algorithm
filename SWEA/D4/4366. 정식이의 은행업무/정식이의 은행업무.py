
'''
2진수와 3진수 각각의 수에서 단 한자리만 잘못 기억하고 있음
2진수 숫자 가져와서 하나씩 바꾸면서 그걸 10진수로 바꿈
3진수 숫자 가져와서 하나씩 바꾸면서 그걸 10진수로 바꿈

'''
def bina_to_int(arr):
    x = 0
    for i in range(len(arr)-1, -1, -1):
        x += arr[i] * (2**(len(arr)-1-i))
    return x

def trit_to_int(arr):
    x = 0
    for i in range(len(arr)-1, -1, -1):
        x += arr[i] * (3**(len(arr)-1-i))
    return x


T = int(input())
for tc in range(1, T+1):
    # n1 : 정식이가 기억하는 송금액의 이진수
    n1 = list(map(int, input()))
    # n2 : 정식이가 기억하는 송금액의 삼진수
    n2 = list(map(int, input()))
    n1_list = []
    binary = {1:0, 0:1}
    trit = {0:[1,2,0], 1:[0, 2, 1], 2:[0, 1, 2]}
    for i in range(len(n1)):
        n1[i] = binary[n1[i]]
        n1_list.append(bina_to_int(n1))
        n1[i] = binary[n1[i]]

    check = False
    for i in range(len(n2)):
        k = n2[i]
        for j in range(3):
            n2[i] = trit[k][j]
            if j !=2:
                tritt = trit_to_int(n2)
                # print(tritt)
                if tritt in n1_list:
                    print(f'#{tc} {tritt}')
                    check = True
                    break
        if check is True:
            break



