k = int(input())
n = int(input())
end = list(input())
start = sorted(end)
ladder = [list(input()) for _ in range(n)]
ladderS = []
ladderE = []
#?를 기준으로 사다리 나누기
for i in range(len(ladder)):
  if ladder[i][0] == '?':
    ladderS = ladder[:i]
    ladderE = ladder[i+1:]
    break
# ????만나기 전까지 사디리 타고 내려오기
for lad in ladderS:
  for i in range(k-1):
    if lad[i] == "-":
      start[i],start[i+1] = start[i+1],start[i]
# 도착 지점에서 ????만나기 전까지 사다리 타고 내려오기
ladderE.reverse()
for lad in ladderE:
  for i in range(k-1):
    if lad[i] == "-":
      end[i],end[i+1] = end[i+1],end[i]
# 두 배열 비교해서 사다리 만들기
answer = []
for i in range(len(start)-1):
  if start[i]==end[i]:
    answer.append("*")
  else:
    if start[i]==end[i+1]:
      answer.append("-")
    elif i!=0 and start[i]==end[i-1]:
      answer.append("*")
    else:
      answer = ['x' for _ in range(k-1)]
      break
#정답
print(''.join(answer))