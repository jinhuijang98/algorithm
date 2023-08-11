n = int(input())



# 5로 먼저 나누고 몫과 나머지 저장
if n % 5 == 0:
    print(n//5)
else:
    rls_5 = n // 5  # 5로 나눈 몫
    cnt_5 = n % 5   # 5로 나눈 나머지
    if cnt_5 == 3:
        print(rls_5 + 1)
    else:
        while True:
            rls_5 -= 1
            cnt_5 += 5
            if rls_5 < 0:
                print(-1)
                break
            if cnt_5 % 3 == 0:
                print(rls_5 + cnt_5//3)
                break