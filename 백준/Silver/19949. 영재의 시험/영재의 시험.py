
def backtracking(cnt):
    # 기저 조건
    global result
    # 숫자 10개를 골랐을 때 종료
    if cnt == 10:
        # 맞춘 개수
        rlt = 0
        # 영재의 답안과 실제 답안을 비교하며 같으면 rlt += 1
        for i in range(10):
            if arr[i] == path[i]:
                rlt += 1
        # 5점 이상이라면
        if rlt >= 5:
            # result에 += 1
            result += 1
        # return을 여기에 달아줘야 함..
        # 들여쓰기 해서 넣을 경우 rlt가 5이상인 경우에만 return되기 때문..
        return

    for num in range(1, 6):
        # 중복된 숫자 제거 - 여기에서는 3번 연속 같은 숫자가 나올 수 없으므로 이걸 조건으로 걸기
        # if cnt >=2 and path[cnt] == path[cnt-1] and path[cnt] == path[cnt-2]:
        #     continue
        if cnt >= 2 and path[cnt-1] == path[cnt-2] == num:
            continue
        # 들어가기 전 로직 - 경로 저장
        path.append(num)
        # path[cnt] = path[cnt-5]
        # 다음 재귀 함수 호출
        backtracking(cnt + 1)
        # 돌아와서 할 로직 (초기화)
        path.pop()




arr = list(map(int, input().split()))

'''
전체 경우의 수 - 0, 1, 2, 3, 4점일 경우의 수
5^7 * 4^3
'''
# 영재의 답안 = path
path = []
result = 0
backtracking(0)
print(result)