import sys

k, l = map(int, sys.stdin.readline().split())

# 수강신청이 들어온 순서대로 학번과 순서를 딕셔너리에 Key, Value로 저장
dict = {}
for i in range(l):
    dict[sys.stdin.readline().rstrip()] = i

# 순서를 기준으로 오름차순 정렬
result = sorted(dict.items(), key = lambda x:x[1])

# 제한 인원보다 신청 인원이 적을 경우
if (k > len(result)):
    # 제한 인원을 신청 인원과 동일하게 수정
    k = len(result)

# 학번을 제한 인원만큼 출력
for i in range(k):
    print(result[i][0])