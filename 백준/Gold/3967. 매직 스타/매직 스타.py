from collections import defaultdict
# defaultdict란 일반적인 딕셔너리와 유사하지만, 키가 존재하지 않을 경우 기본값 갖도록 설정할 수 있음


# 입력 받기
s = [list(str(input())) for _ in range(5)]
star = ['' for _ in range(12)]
idx = 0
visited = defaultdict(bool)

# 주어진 매직 스타 부분을 별도의 배열에 저장
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            star[idx] = s[i][j]
            idx += 1
            if s[i][j] != 'x':
                visited[s[i][j]] = True

# 알파벳 리스트 생성
apb = [chr(i) for i in range(ord('A'), ord('L')+1)]

# 매직 스타의 조건을 확인하는 함수
def chk():
    if not (ord(star[0]) + ord(star[2]) + ord(star[5]) + ord(star[7]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[2]) + ord(star[3]) + ord(star[4]) == 22 + ord('A')*4):
        return False
    if not (ord(star[0]) + ord(star[3]) + ord(star[6]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[7]) + ord(star[8]) + ord(star[9]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[5]) + ord(star[8]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    if not (ord(star[4]) + ord(star[6]) + ord(star[9]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    return True

ans = []
flag = False

# 재귀적으로 매직 스타를 채우는 함수
def magic_star(cur, mstar):
    global ans, flag
    if flag:
        return
    if cur == 12:
        # 매직 스타 조건을 만족하는지 확인 후 결과 저장
        if chk():
            flag = True
            ans = mstar[:]
        return
    if mstar[cur] != 'x':
        # 이미 알파벳이 채워진 경우, 다음 인덱스로 이동
        magic_star(cur+1, mstar)
    else:
        # 알파벳이 채워지지 않은 경우, 가능한 알파벳을 시도
        for i in range(len(apb)):
            if not visited[apb[i]]:
                mstar[cur] = apb[i]
                visited[apb[i]] = True
                magic_star(cur+1, mstar)
                visited[apb[i]] = False
                mstar[cur] = 'x'
                if flag:
                    return

# 매직 스타 찾기
magic_star(0, star)

idx = 0

# 찾은 매직 스타를 기존 배열에 대입하여 결과 출력
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            s[i][j] = ans[idx]
            idx += 1

# 결과 출력
for i in range(5):
    print(''.join(s[i]))