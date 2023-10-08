# 16943 숫자 재배치

a, b = input().split()
'''
a에 포함된 숫자의 순서를 섞어서 새로운 수 c를 만들려고 함
c는 a의 순열 중 하나
가능한 c 중에서 b보다 작으면서 가장 큰 값 구하기
c는 0으로 시작하면 안됨!
만약 c가 없을 경우 -1 출력

'''
arr1 = list(map(int, a))
# arr2 = list(map(int, b))

arr1.sort(reverse=True)


path = [-1] * len(arr1)
rlt = 0
visited = [False] * len(arr1)
def back(cnt):
    global rlt
    if cnt == len(arr1):
        result = ''
        for j in range(cnt):
            result += str(path[j])
        if result[0] != '0' and int(result) < int(b):
            rlt = int(result)

    if rlt != 0:
        return

    remember = -1
    for i in range(len(arr1)):
        # if arr1[i] in path:
        #     continue
        if not visited[i] and remember != arr1[i]:
            visited[i] = True
            remember = arr1[i]

            path[cnt] = arr1[i]
            back(cnt+1)
            visited[i] = False
            path[cnt] = -1

back(0)
if rlt == 0:
    print(-1)
else:
    print(rlt)
