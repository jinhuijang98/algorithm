N= int(input())
# N을 ~의 제곱합으로 표현

x = int(N**(1/2))
cnt =0
if x**2 == N:
    cnt = 1
else:
    for i in range(1, x+1):
        ii = i**2
        if int((N-ii) ** 0.5) == (N-ii) ** 0.5:
            cnt = 2
            break
    else:
        for i in range(1, x+1):
            ii = i**2
            for j in range(1, int((N-ii)**0.5)+1):
                jj = j**2
                if int((N-ii-jj) ** 0.5)==(N-ii-jj) ** 0.5 :
                    cnt = 3
                    break
if cnt == 0:
    print(4)
else:
    print(cnt)