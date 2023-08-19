import sys

N = int(sys.stdin.readline())  # 명령 수
Q = [0] * (N+1)  # 큐
front = -1
rear = -1  # 초기값 설정


def enq(item):
    global rear

    rear += 1
    Q[rear] = item


def deq():
    global front
    global rear
    if front == rear:
        print(-1)
    else:
        front += 1
        print(Q[front])


for _ in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push':
        enq(order[1])

    elif order[0] == 'pop':
        deq()

    elif order[0] == 'size':
        print(rear - front)

    elif order[0] == 'empty':
        if rear == front:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if rear == front:
            print(-1)
        else:
            print(Q[front+1])

    elif order[0] == 'back':
        if rear == front:
            print(-1)
        else:
            print(Q[rear])