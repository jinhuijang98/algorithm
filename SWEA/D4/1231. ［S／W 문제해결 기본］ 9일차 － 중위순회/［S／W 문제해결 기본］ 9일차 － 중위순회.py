

def inorder(p, N):
    if p <= N:
        inorder(p*2, N)    # 왼쪽 자식 순회
        print(tree[p], end= '')
        inorder(p*2 +1, N)  # 오른쪽 자식 순회





for tc in range(1, 11):
    # N : 정점의 총 수
    N = int(input())
    # tree
    tree = [0] * (N+1)
    for _ in range(N):
        arr = list(input().split())
        # tree에 W, F, ...와 같은 값을 넣음
        tree[int(arr[0])] = arr[1]
    # 다 넣고 나서 중위 순회
    print(f'#{tc}', end=' ')
    inorder(1, N)
    print()