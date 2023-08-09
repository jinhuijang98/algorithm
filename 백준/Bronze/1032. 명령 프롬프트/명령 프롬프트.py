N = int(input())
# 처음 값만 가져와서 list로 만들고 검사
arr = list(input())
# new_arr = arr.copy()

# word에 가져와서
for i in range(N-1):
    word = list(input())
    
    for j in range(len(arr)):
        if word[j] != arr[j]:
            arr[j] = "?"


# 그냥 이렇게 해도 출력 결과 동일하게 나옴
print(''.join(arr))