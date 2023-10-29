s=input()
p=input()

char=dict()

# 각 문자에 대한 index 저장
for i in range(len(s)):
    char[s[i]]=char.get(s[i],[])+[i]

index=0
answer=0
len_s=len(p)

# 결국 이 while문을 몇 번이나 돌았나? 가 문제의 정답이 된다.
while index<len_s:
    arr=char[p[index]]

    cnt=0

    # 가장 같은 부분이 긴 부분 찾기
    for i in range(len(arr)):
        idx=arr[i]
        temp=0
        temp_index=index
        while idx<len(s) and temp_index<len_s:
            if s[idx]==p[temp_index]:
                idx+=1
                temp_index+=1
                temp+=1
            else:
                break
        cnt=max(cnt,temp)
        
    
    answer+=1
    index+=cnt
    

print(answer)