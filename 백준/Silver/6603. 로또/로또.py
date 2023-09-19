import sys
input = sys.stdin.readline

def subset(i, N):
    if i == k:
        if sum(bit) == N:
            for j in range(k):
                if bit[j] == 1:
                    print(S[j], end =' ')
            print()
            return
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)
    return

while True:
    k, *S = map(int, input().strip().split())
    if k!= 0:
        # print(k)
        # print(S)
        # k개에서 6개를 골라
        bit = [0] * k
        subset(0, 6)
        print()
    else:
        break
