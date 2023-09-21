import sys
input = sys.stdin.readline
# n : 가희가 메모장에 적은 키워드 개수
# m : 가희가 블로그에 쓴 글의 개수
n, m = map(int, input().strip().split())

keyword = set([input().strip() for _ in range(n)])
# print(keyword)

for _ in range(m):
    sett =input().strip().split(',')
    for j in sett:
        keyword.discard(j)
    print(len(keyword))