import sys
input = sys.stdin.readline
n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
# print(arr)
# print(n)
'''
동준이는 게임 만듦 
-> 게임 총 N개의 레벨
각 레벨 클리어할 때마다 점수
플레이어 점수 : 레벨을 클리어하면서 얻은 점수의 합
이 점수로 온라인 순위 매김
동준이는 레벨 난이도 순으로 배치
하지만, 실수로 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우 만듦

그래서 특정 레벨의 점수 감소
-> 각 레벨을 클리어할 때 주는 점수가 증가하게
각 레벨을 클리어할 때 얻는 점수가 주어졌을 때, 몇 번 감소시키며 ㄴ되는지?
점수는 항상 양수, 1만큼 감소하는 것이 1번
최소한

'''
cnt = 0
for i in range(n-1, -1, -1):        # i를 뒤에서부터 비교
    for j in range(i-1, -1, -1):    # j도 i-1, ..., 0까지 비교해가면서
        while arr[i] <= arr[j]:     # 작아질때까지
            arr[j] -= 1
            cnt += 1                # cnt += 1
print(cnt)