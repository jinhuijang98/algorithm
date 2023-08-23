import sys
input = sys.stdin.readline

# n : 땅의 개수 (이진 트리)
# q : 오리 수
n, q = map(int, input().strip().split())

# arr => i번째 오리가 원하는 땅 번호
arr = []
for i in range(q):
    x = int(input().strip())
    arr.append(x)

tree = [0]*(n+1)        # 값을 담을 배열

# print(arr)          # [3, 5, 6, 2]
# 만약 현재 값이 이전 값을 다 검사해봤을 때 그 숫자의 자식이라면 부모 값 출력
# 할아버지 할머니 일수도

for i in range(q):
    result = []
    x = arr[i]
    # if tree[arr[i]] == 0:
    if tree[x] == 1:
        result.append(x)

    while x//2 > 1:
        x = x//2
        if tree[x] == 1:
            result.append(x)

    if result:
        print(result[-1])
    else:
        tree[arr[i]] = 1
        print(0)



'''
1. arr의 현재값과 이전값 비교
2. (1) 만약 arr의 현재값이 이전값과 같다면 arr의 이전값 출력 and break
    (2) 다르다면 현재값 //2 해서 다시 이전값과 비교
3. (1) 만약 같은게 존재한다면 이전값 출력 and break
    (2) 만약 다르다면 다시 현재값//2(>0) 해서 이전값과 비교
4. 다 끝났는데 못찾았다면 0출력 + index +=1

'''
