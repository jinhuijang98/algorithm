# 다시
n = int(input())
data = sorted(list(map(int,input().split())))
if n>2:
    result = 2
    for start in range(n-2):
        end = start+2
        while True:
            if data[start] + data[start+1] > data[end]:
                result = max(result, end-start+1)
                end+=1
                if end==n:break
            else:break
    print(result)
else:print(n)