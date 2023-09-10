import sys
input = sys.stdin.readline

# 굴다리의 길이
n = int(input().strip())

# 가로등의 개수
m = int(input().strip())

# m개의 설치할 수 있는 가로등의 위치 (오름차순, 중복x, 정수)
arr = list(map(int, input().strip().split()))

'''
각 가로등은 높이만큼 주위를 비출 수 있다. 
하지만 갑자기 예산이 부족해진 인천광역시는 가로등의 높이가 높을수록 가격이 비싸지기 때문에 
최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다
최소한의 예산이 들 높이를 구하자. 단 가로등은 모두 높이가 같아야
가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다
'''
# flag = 1
# 1부터 시작해서
# m1 - flag ~ m1 + flag까지
# m2 - flag + m2 + flag까지
# ...
# mn - flag + mn - flag까지


last, heights = arr[0], arr[0]

for i in range(1, len(arr)):
    tmp = abs(last - arr[i])

    if tmp % 2 == 0:
        tmp = tmp // 2
    else:
        tmp = (tmp // 2) + 1

    heights = max(heights, tmp)

    last = arr[i]

heights = max(heights, abs(n - arr[len(arr) - 1]))

print(heights)