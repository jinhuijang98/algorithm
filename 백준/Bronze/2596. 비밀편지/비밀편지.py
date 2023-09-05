import sys

input = sys.stdin.readline

# 보낸 문자의 개수
n = int(input().strip())

# input에서 6씩 잘라서 리스트에 저장
text = input().strip()

arr = []
i = 0
while i < 6 * n:
    arr.append(text[i:i+6])
    i += 6
# A ~ H 딕셔너리로 저장
dic = {'000000' : 'A',
       '001111' : 'B',
       '010011' : 'C',
       '011100' : 'D',
       '100110' : 'E',
       '101001' : 'F',
       '110101' : 'G',
       '111010' : 'H'}
# 키들을 리스트로 저장
check = list(dic.keys())


result = []
for i in range(n):
    for j in range(8):
        cnt = 0
        for k in range(6):
            if arr[i][k] != check[j][k]:
                cnt += 1
            if cnt == 2:
                break
        if cnt < 2:
            result.append(dic[check[j]])
            break
    else:
        # 다 돌았는데도 cnt < 2 를 찾지 못했다면 그 순서를 출력하고 break
        print(i+1)
        break
# 최종 결과값은 result의 길이와 arr의 길이가 같아야 하므로 이럴 경우 print
if len(result) == len(arr):
    for i in range(n):
        print(result[i], end='')