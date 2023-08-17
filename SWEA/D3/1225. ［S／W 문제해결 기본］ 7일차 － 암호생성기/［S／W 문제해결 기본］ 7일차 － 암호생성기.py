for tc in range(1, 11):
    T = int(input())
    front = -1
    # rear = -1
    arr = list(map(int, input().split()))
    # 확인 값 check로 두기
    check = True
    while check:
        for i in range(1, 6):     #
            front += 1
            front = front % 8
            # 0일 때도 종료가 되어야 하니까 >= 아니라 >여야 함!!
            if arr[front] - i > 0:
                arr[front] = arr[front] - i
            else:
                arr[front] = 0
                check = False
                break
    new_list = []
    for i in range(8):
        x = front+1 + i
        x = x % 8
        new_list.append(str(arr[x]))
    rlt=' '.join(new_list)
    print(f'#{tc} {rlt}')